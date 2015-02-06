#!/usr/bin/env python
import os
import fcntl
import struct
from datetime import datetime
from time import sleep, strftime
import daemon

def getWeightInGrams(dev="/dev/dymo_scale"):
    """
    The default param passed in assumes that the accompanying file 51-usb-scale.rules
    rule file has been added to /etc/udev/rules.d to automatically map this specific
    scale to the /dev/dymo_scale device handle. Otherwise, this device normally 
    appears on /dev/usb/hiddev0
    """
    fd = os.open(dev, os.O_RDONLY)

    # Read 4 unsigned integers from USB device
    hiddev_event_fmt = "IIII"
    usb_binary_read = struct.unpack(hiddev_event_fmt, os.read(fd, struct.calcsize(hiddev_event_fmt)))
    return usb_binary_read[3]

def main():
    while True:
        print("{0},{1}".format(datetime.utcnow().strftime("%Y-%m-%d_%X"), getWeightInGrams()))
        sleep(1)

if __name__ == "__main__":
    main()
    # with daemon.DaemonContext():
    #     main()


