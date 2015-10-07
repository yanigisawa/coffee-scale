#!/usr/bin/env python
import os
import fcntl
import struct
from datetime import datetime, timedelta
from time import sleep, strftime
import logging
from logging.handlers import TimedRotatingFileHandler
import glob
import shutil
from ISStreamer.Streamer import Streamer
import hipchat
import math
import requests
import json


class CoffeeScale:
    def __init__(self):
        self._logger = logging.getLogger("coffee_log")
        self._logger.setLevel(logging.INFO)
        self._currentWeight = 0
        self._weightChangedThreshold = 5
        self._emptyPotThreshold = 10
        self._loopCount = 0
        self._logToHipChatLoopCount = 40
        self._initialStateKey = ''
        self._environment = ''
        self._hipchatKey = ''
        self._ledServiceUrl = ''
        self._mostRecentLiftedTime = datetime.now()
        # When Adjusting the Pot Weight, you may also need to adjust the
        # 'calculateMugAmounts' value. Pass the full pot weight into
        # that method to automatically calculate mug capacity per pot.
        self._potWeight = 898
        self._mugFluidCapacity = 266
        # The getLedMessage no longer cares what the 
        # full pot capacity is. It will simply display "X mugs - Wed 08:14"
        self._mugAmounts = self.calculateMugAmounts(9999) # Full pot capacity

    @property
    def initialStateKey(self):
        if not self._initialStateKey:
            self._initialStateKey = os.environ.get('INITIAL_STATE_ACCESS_KEY')
            if not self._initialStateKey:
                self._logger.error("### Initial State Key not set in environment variable")

        return self._initialStateKey

    @property
    def environment(self):
        if not self._environment:
            self._environment = os.environ.get("ENVIRONMENT")
            if not self._environment:
                self._environment = "prod"

        return self._environment

    @property
    def hipchatKey(self):
        if not self._hipchatKey:
            self._hipchatKey = os.environ.get('HIPCHAT_KEY')
            if not self._hipchatKey:
                self._logger.error('### Hipchat API Key missing from environment variable HIPCHAT_KEY')

        return self._hipchatKey

    @property
    def ledServiceUrl(self):
        if not self._ledServiceUrl:
            self._ledServiceUrl = os.environ.get('LED_SERVICE_URL')
            if not self._ledServiceUrl:
                self._logger.error('### LED_SERVICE_URL environment variable has not been set') 

        return self._ledServiceUrl

    def calculateMugAmounts(self, maxPotWeight):
        weight = self._potWeight + self._mugFluidCapacity
        mugAmounts = []
        while weight < maxPotWeight:
            mugAmounts.append(weight)
            weight += self._mugFluidCapacity

        return mugAmounts

    def configureLogFile(self):
        logFile = "/var/log/coffee"
        rotateInterval = 60
        handler = TimedRotatingFileHandler(logFile,
                when="m", interval=rotateInterval, utc=True)

        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        self._logger.addHandler(handler)

    def shouldLogWeight(self, newReading):
        return abs(self._currentWeight - newReading) > self._weightChangedThreshold

    def potIsLifted(self):
        return self._currentWeight <= self._emptyPotThreshold

    def shouldPostToHipChat(self):
        return self._loopCount == self._logToHipChatLoopCount

    def getHipchatParameters(self):
        parameters = {}
        # Fridge Room
        parameters['room_id'] = 926556
        totalAvailableMugs = len(self._mugAmounts)
        parameters['from'] = "{0} / {1}".format(self.getAvailableMugs(), totalAvailableMugs)
        parameters['message'] = "{0} / {1}".format(self._currentWeight, self._mugAmounts[totalAvailableMugs - 1]) 
        parameters['color'] = 'random'

        return parameters

    def getAvailableMugs(self):
        coffeeWeight = self._currentWeight - self._potWeight
        availableMugs = int(math.floor((coffeeWeight + (coffeeWeight * 0.1)) / self._mugFluidCapacity))

        return availableMugs

    def getWeightInGrams(self, dev="/dev/usb/hiddev0"):
        """
        This device normally appears on /dev/usb/hiddev0, assume
        device still appears on this file handle.
        """
        # If we cannot find the USB device, return -1

        grams = -1
        try:
            fd = os.open(dev, os.O_RDONLY)

            # Read 4 unsigned integers from USB device
            hiddev_event_fmt = "IIII"
            usb_binary_read = struct.unpack(hiddev_event_fmt, os.read(fd, struct.calcsize(hiddev_event_fmt)))
            grams = usb_binary_read[3]
            os.close(fd)
        except OSError as e:
            print("{0} - Failed to read from USB device".format(datetime.utcnow()))
        return grams

    def moveLogsToArchive(self, tempFilePath, archiveDir):
        """
        Using shutil.move here since the raspberry pi will 
        be moving the files from a tempfs file system to the
        ext3 file system on the SD card. 
        """
        tempFileName = os.path.basename(tempFilePath)
        tempFileDir = os.path.dirname(tempFilePath)
        logFiles = glob.glob("{0}.*".format(tempFilePath))

        for fileName in logFiles:
            shutil.move(fileName, os.path.join(archiveDir, os.path.basename(fileName)))

    def shouldPostToLed(self):
        return self._loopCount == self._logToHipChatLoopCount

    def getLedMessage(self):
        available_mugs = self.getAvailableMugs()
        return "{0} mug{2} - {1}".format(available_mugs,
                self._mostRecentLiftedTime.strftime("%a %H:%M"), 
                "" if available_mugs == 1 else "s")

    def postToLed(self):
        displayJson = {}
        totalAvailableMugs = len(self._mugAmounts)
        displayJson['text'] = self.getLedMessage()

        url = "{0}/display".format(self.ledServiceUrl)
        payload = json.dumps(displayJson)
        headers = {'content-type': 'application/json'}

        response = requests.post(url, data=payload, headers=headers, timeout=5)

    def logToInitialState(self):
        utcnow = datetime.utcnow()
        bucketKey = "{0} - coffee_scale_data".format(self.environment)

        streamer = Streamer(bucket_name="{0} - Coffee Scale Data".format(self.environment), 
                bucket_key=bucketKey, access_key=self.initialStateKey)

        if self.potIsLifted():
            streamer.log("Coffee Pot Lifted", True)
        streamer.log("Coffee Weight", self._currentWeight)
        streamer.close()

    def writeToHipChat(self):
        hipster = hipchat.HipChat(token=self.hipchatKey)
        params = getHipchatParameters()
        hipster.method('rooms/message', method='POST', parameters=params)

    def main(self):
        self._currentWeight = self.getWeightInGrams()

        while True:
            try:
                self._loopCount += 1
                tmpWeight = self.getWeightInGrams()

                if self.shouldLogWeight(tmpWeight):
                    self._logger.info(
                            "{0},{1}".format(datetime.utcnow().strftime("%Y-%m-%dT%X"), tmpWeight))
                    self._currentWeight = tmpWeight
                    self.logToInitialState()

                if self.shouldPostToLed():
                    self._loopCount = 0
                    self.postToLed()

                if self.potIsLifted():
                    self._mostRecentLiftedTime = datetime.now()

            except Exception as e:
                self._logger.error(e)

            # if self.shouldPostToHipChat():
            #     self._loopCount = 0
            #     self.writeToHipChat()

            sleep(1)

if __name__ == "__main__":
    scale = CoffeeScale()
    scale.configureLogFile()
    scale.main()
