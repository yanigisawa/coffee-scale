import redis
import threading
import time
import os
import logging
from subprocess import Popen
import signal


class Worker(threading.Thread):
    def __init__(self, module = None):
        threading.Thread.__init__(self)
        self.pythonModule = module

    def run(self):
        path = '/home/pi/src/coffee-scale/pubsub/animation/{0}'.format(self.pythonModule)
        args = ['python', path, '--led-no-hardware-pulse', '1', '-r', '16']
        self.p = Popen(args)


    def halt(self):
        log.debug('send terminate')
        self.p.terminate()

class Listener(threading.Thread):
    def __init__(self, r, channels):
        threading.Thread.__init__(self)
        self.redis = r
        self.pubsub = self.redis.pubsub(ignore_subscribe_messages = True)
        self.pubsub.subscribe(channels)
        self._worker = None
    
    def work(self, item):
        className = '{0}'.format(item['data'])
        self._worker = Worker(className)
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
                del self._worker
                self._worker = None

            if item['data'] == 'KILL':
                log.debug('received kill message')
                self.pubsub.unsubscribe()
                break
            elif item['data'] == 'STOP':
                pass
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
