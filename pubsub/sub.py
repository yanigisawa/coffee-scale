import redis 
import time 

r = redis.StrictRedis(host='localhost', port=6379, db=0)
p = r.pubsub()
p.subscribe('test')

while True:
    message = p.get_message()
    if message:
        print "Subscriber: %s" % message['data']
    time.sleep(2)
