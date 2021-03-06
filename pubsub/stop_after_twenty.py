#!/usr/bin/env python

import redis
import time
import os

redis = redis.StrictRedis(host='localhost', port=6379, db=0)

time.sleep(20)

queue = os.environ.get('REDIS_ANIMATION_QUEUE')
redis.publish(queue, 'STOP')
