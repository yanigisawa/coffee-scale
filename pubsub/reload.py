
#!/usr/bin/env python

import redis
import time
import os

redis = redis.StrictRedis(host='localhost', port=6379, db=0)
channel = redis.pubsub()

queue = os.environ.get('REDIS_ANIMATION_QUEUE')
redis.publish(queue, 'RELOAD')
