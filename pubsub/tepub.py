#!/usr/bin/env python

import redis
import time
import os
import json

redis = redis.StrictRedis(host='localhost', port=6379, db=0)
channel = redis.pubsub()

queue = os.environ.get('REDIS_ANIMATION_QUEUE')
process = {}
process['moduleName'] = 'fixed-text.py'
process['args'] = '-t 4 mugs::11:33'
redis.publish(queue, json.dumps(process))
