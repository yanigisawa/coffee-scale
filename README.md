# Coffee Scale #

Simple python code base to read binary data from a [Dymo M10 scale](http://www.amazon.com/DYMO-1772057-Digital-Shipping-10-pound/dp/B0053HCWRE)

### File List ###

* coffe_scale.py - Main entry point for reading data from the scale
* 51-user-scale.rules - udev file to be placed at /etc/udev/rules.d to automatically map /dev/usb/hiddev0 to /dev/dymo_scale
* usescale.py - Reference python implementation lifted [from here.](http://www.thok.org/intranet/python/usb/index.html) Included here as a reference in case it is needed in the future for future scale reverse engineering.

