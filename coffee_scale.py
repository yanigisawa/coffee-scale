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

logger = logging.getLogger("coffee_log")
logger.setLevel(logging.INFO)

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
        
def main(args):

    rotateMinutes = timedelta(minutes = args.logRotateTimeMinutes)
    rotateTime = datetime.utcnow() + rotateMinutes
    currentWeight = getWeightInGrams()

    while True:
        if datetime.utcnow() > rotateTime:
            moveLogsToArchive(args.tempFile, args.permanentDirectory)
            rotateTime = datetime.utcnow() + rotateMinutes
        if getWeightInGrams() != currentWeight:
            logger.info("{0},{1}".format(datetime.utcnow().strftime("%Y-%m-%dT%X"), getWeightInGrams()))
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


