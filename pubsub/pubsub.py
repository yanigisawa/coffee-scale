import redis
import threading
import time
import os
import logging
from subprocess import Popen
import signal
import json


class Worker(threading.Thread):
    def __init__(self, module = None, args = None):
        threading.Thread.__init__(self)
        self.pythonModule = module
        self.args = args

    def run(self):
        path = os.path.abspath('animation/{}'.format(self.pythonModule))
        process = ['python', path, '--led-no-hardware-pulse', '1', '-r', '16']
        if self.args != None:
            process.append(self.args)
        log.debug('Running {0}'.format(process))
        self.p = Popen(process)


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
        data = json.loads(item['data'])
        className = '{0}'.format(data['moduleName'])
        args = None
        if 'args' in data.keys():
            args = data['args']
        self._worker = Worker(className, args)
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

            if item['data'].upper() == 'KILL':
                log.debug('received kill message')
                self.pubsub.unsubscribe()
                break
            elif item['data'].upper() == 'STOP':
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
