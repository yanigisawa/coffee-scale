#!/usr/bin/python
import os
import fcntl
import struct

# inspired by http://kubes.org/src/usbscale.c

def open_hid(dev="/dev/usb/hiddev0"):
    fd = os.open(dev, os.O_RDONLY)
    # #define _IOC_NRBITS	8
    # #define _IOC_TYPEBITS	8
    # define _IOC_SIZEBITS	14
    # define _IOC_DIRBITS	2
    # #define _IOC_NRSHIFT	0
    # #define _IOC_TYPESHIFT	(_IOC_NRSHIFT+_IOC_NRBITS)
    # -> 8
    # #define _IOC_SIZESHIFT	(_IOC_TYPESHIFT+_IOC_TYPEBITS)
    # -> 16
    # #define _IOC_DIRSHIFT	(_IOC_SIZESHIFT+_IOC_SIZEBITS)
    # -> 30
    # 
    # asm/generic.h: define _IOC_READ 2U
    #  #define _IOC(dir,type,nr,size) \
    #      (((dir)  << _IOC_DIRSHIFT) | \
    #       ((type) << _IOC_TYPESHIFT) | \
    #       ((nr)   << _IOC_NRSHIFT) | \
    #       ((size) << _IOC_SIZESHIFT))
    def _IOC(iodir, iotype, ionr, iosize):
        return (iodir << 30) | (iotype << 8) | (ionr << 0) | (iosize << 16)
    # linux/hiddev.h: #define HIDIOCGNAME(len) _IOC(_IOC_READ, 'H', 0x06, len)
    def HIDIOCGNAME(len):
        return _IOC(2, ord("H"), 6, len)
    # ioctl(fd, HIDIOCGNAME(100), name);
    name = fcntl.ioctl(fd, HIDIOCGNAME(100), " "*100).split("\0",1)[0]

    # struct hiddev_event ev[EV_NUM=8];
    # struct hiddev_event {
    # 	unsigned hid;
    # 	signed int value;
    # };
    hiddev_event_fmt = "Ii"
    # read(fd, ev, sizeof(struct hiddev_event) * EV_NUM);
    ev = []
    for _ in range(8):
        ev.append(struct.unpack(hiddev_event_fmt, os.read(fd, struct.calcsize(hiddev_event_fmt))))
    # print ev
    input_large = ev[6][1]
    input_small = ev[7][1]
    return name, input_small % 256, input_large % 256

def tare(inputs):
    return max(inputs)

if __name__ == "__main__":
    scale_factor = 2.6666667 # ha ha

    print open_hid()
    smalls = []
    larges = []
    for _ in range(5):
        name, small, large = open_hid()
        smalls.append(small)
        larges.append(large)
    base_small = max(smalls)
    print smalls, "->", base_small
    base_large = max(larges)
    print larges, "->", base_large
    print "Tared..."

    raw_input("put something on:")

    name, small, large = open_hid()
    if large < base_large + 1:
        large = 0
    else:
        large = ((large - (base_large + 1)) * 94) + ((256 - base_small) / scale_factor)

    if large == 0:
        if small >= base_small:
            small = (small - base_small) / scale_factor
        else:
            small = 0
    else:
        small = (small - base_small) / scale_factor

    final = large + small
    print final

# t-mobile g1 is "158g w/battery (5.6oz)", I get 146, 149
# leatherman skeletool is 5oz/142g", I get 131, 132
# a US Quarter is 5.670 g according to http://www.usmint.gov/about_the_mint/index.cfm?flash=no&action=coin_specifications
#   I get 5.25, 5.6
# a dime is 2.268 g according to the same page; I get 1.5, 1.8
