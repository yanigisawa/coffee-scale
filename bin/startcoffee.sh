#!/bin/bash
. /root/env.sh
echo $(($$ + 1)) > /var/run/coffee.pid
/root/coffee-scale/venv/bin/python /root/coffee-scale/src/coffee_scale.py 1>/var/log/coffee 2>&1
