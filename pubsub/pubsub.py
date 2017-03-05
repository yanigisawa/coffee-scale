import redis
import threading
import time
from animation import *
import os
import logging


class Worker(threading.Thread):
    def __init__(self, animation = None):
        threading.Thread.__init__(self)
        self.animation = animation

    def run(self):
        self.animation.run()

    def halt(self):
        log.debug('called halt')
        self.animation.set_halt()

class Listener(threading.Thread):
    def __init__(self, r, channels):
        threading.Thread.__init__(self)
        self.redis = r
        self.pubsub = self.redis.pubsub(ignore_subscribe_messages = True)
        self.pubsub.subscribe(channels)
        self._worker = None
    
    def work(self, item):
        className = '{0}()'.format(item['data'])
        animation = eval(className)
        self._worker = Worker(animation)
        self._worker.start()
    
    def run(self):
        for item in self.pubsub.listen():
            log.debug('listen on queue')
            log.debug('_worker: {0}'.format(self._worker))
            if self._worker != None:
                # Halt the previous animation, and join that thread
                # to wait until thread has properly cleaned up
                self._worker.halt()
                self._worker.join()

            if item['data'] == 'KILL':
                log.debug('received kill message')
                self.pubsub.unsubscribe()
                break
            # elif item['data'] == 'RELOAD':
            #     from animations import *
            else:
                self.work(item)

if __name__ == "__main__":
    console = logging.StreamHandler()
    log = logging.getLogger()
    log.addHandler(console)
    log.setLevel(logging.DEBUG)
    queue = os.environ.get('REDIS_ANIMATION_QUEUE')
    client = Listener(redis.Redis(), [queue])
    client.start()
    
    # r = redis.Redis()
    # r.publish('test', 'this will reach the listener')
    # r.publish('fail', 'this will not')
    # 
    # for i in range(10):
    #     r.publish('test', 'another message for {0}'.format(i))
    #     time.sleep(1)
	
    # time.sleep(10)
    # r.publish('test', 'KILL')
