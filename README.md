# Coffee Scale #

Simple python code base to read binary data from a [Dymo M10 scale](http://www.amazon.com/DYMO-1772057-Digital-Shipping-10-pound/dp/B0053HCWRE)

### Example Usage ###

1. Setup a Raspberry Pi running Raspbian

2. Create a virtualenv using the dependencies from requirements.txt

  ```
  virtualenv coffeeEnv
  pip install -r requirements.txt
  ```

3. Run the coffee_scale.py script from the virtual environment

  `./coffeeEnv/bin/python coffee_scale.py 1>/var/log/coffee 2>&1`
  
The main method in this module will loop forever, and will take a reading off the scale once per second. If you use [monit](https://mmonit.com/monit/) you can use the start and stop scripts from the /bin folder. Note, those scripts assume you're running this scripts as root, and that the source code has been checked out from, and a virtual environment exists in the /root directory. 

I ran this script as root because of the low risk to our isolated Raspberry Pi environment. If desired, you can chown the ownership of the /dev/usb/hiddev0 device to your standard user, and run this script as that standard user.

### Integrations ###

There is built-in support for [initial state](https://www.initialstate.com/) dashboarding. Supply the `INITIAL_STATE_ACCESS_KEY` environment variable with your initial state key, and this code will send weights to your initial state account.

### File List ###

* coffe_scale.py - Main entry point for reading data from the scale
* 51-user-scale.rules - udev file to be placed at /etc/udev/rules.d to automatically map /dev/usb/hiddev0 to /dev/dymo_scale
* usescale.py - Reference python implementation lifted [from here.](http://www.thok.org/intranet/python/usb/index.html) Included here as a reference in case it is needed in the future for future scale reverse engineering.

### References ###

Initial inspiration for this repository was pulled from [this C repo](https://github.com/erjiang/usbscale). The scales.h file was my first stop in finding a scale that would be supported via USB and easily read with either C or Python code.
