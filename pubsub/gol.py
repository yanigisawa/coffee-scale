#!/usr/bin/env python

import redis
import time
import os
import json

redis = redis.StrictRedis(host='localhost', port=6379, db=0)
channel = redis.pubsub()

queue = os.environ.get('REDIS_ANIMATION_QUEUE')
process = {}
# process['moduleName'] = 'gol-red-glider.py'
# process['moduleName'] = 'gol-block-switch.py'
# process['moduleName'] = 'gol-acorn.py'
# process['moduleName'] = 'gol-pent.py'
process['moduleName'] = 'gol-gosper-gun.py'
redis.publish(queue, json.dumps(process))
