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

logger = logging.getLogger("coffee_log")
logger.setLevel(logging.INFO)

_currentWeight = 0
_weightChangedThreshold = 5
_emptyPotThreshold = 10
_initialStateKey = os.environ.get('INITIAL_STATE_ACCESS_KEY')
if not _initialStateKey:
    print("### Initial State Key not set in environment variable")

_environment = os.environ.get("ENVIRONMENT")
if not _environment:
    _environment = "prod"

def getWeightInGrams(dev="/dev/usb/hiddev0"):
    """
    The default param passed in assumes that the accompanying file 51-usb-scale.rules
    rule file has been added to /etc/udev/rules.d to automatically map this specific
    scale to the /dev/dymo_scale device handle. Otherwise, this device normally 
    appears on /dev/usb/hiddev0
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

def moveLogsToArchive(tempFilePath, archiveDir):
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

def shouldLogWeight(newReading):
    return abs(_currentWeight - newReading) > _weightChangedThreshold

def potIsLifted():
    return _currentWeight <= _emptyPotThreshold

def logToInitialState():
    utcnow = datetime.utcnow()
    bucketKey = "{0} - coffee_scale_data".format(_environment)

    streamer = Streamer(bucket_name="{0} - Coffee Scale Data".format(_environment), 
            bucket_key=bucketKey, access_key=_initialStateKey)

    if potIsLifted():
        streamer.log("Coffee Pot Lifted", True)
    streamer.log("Coffee Weight", _currentWeight)
    streamer.close()
        
def main(args):
    rotateMinutes = timedelta(minutes = args.logRotateTimeMinutes)
    rotateTime = datetime.utcnow() + rotateMinutes
    global _currentWeight 
    _currentWeight = getWeightInGrams()

    while True:
        tmpWeight = getWeightInGrams()
        if datetime.utcnow() > rotateTime:
            moveLogsToArchive(args.tempFile, args.permanentDirectory)
            rotateTime = datetime.utcnow() + rotateMinutes

        if shouldLogWeight(tmpWeight):
            logger.info("{0},{1}".format(datetime.utcnow().strftime("%Y-%m-%dT%X"), tmpWeight))
            _currentWeight = tmpWeight
            logToInitialState()


        sleep(1)

def getParser():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('tempFile', help='Temporary output location file to write', 
            default='/var/tmp/coffee_scale')
    parser.add_argument('permanentDirectory', help='Permanent storage location for scale data')
    parser.add_argument('logRotateTimeMinutes', 
            help='Number of minutes to capture data in the temp-file before writing to the permanent directory',
            type=int)

    return parser

if __name__ == "__main__":
    parser = getParser()
    args = parser.parse_args()
    handler = TimedRotatingFileHandler(args.tempFile,
            when="m", interval=args.logRotateTimeMinutes, utc=True)

    logger.addHandler(handler)
    main(args)


