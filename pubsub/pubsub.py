import redis
import threading
import time
import os
import logging
from subprocess import Popen
import signal
import json


class Listener(threading.Thread):
    def __init__(self, r, channels):
        threading.Thread.__init__(self)
        self.redis = r
        self.pubsub = self.redis.pubsub(ignore_subscribe_messages = True)
        self.pubsub.subscribe(channels)
        self._pid = None
    
    def start_process(self, item):
        data = json.loads(item['data'])
        args = None
        className = '{0}'.format(data['moduleName'])
        path = os.path.abspath('pubsub/animation/{}'.format(className))
        process = ['python', path, '--led-no-hardware-pulse', '1', '-r', '16', '--led-pwm-lsb-nanoseconds', '300']
        if 'args' in data.keys() and data['args']:
            a = ['-{0}'.format(y) for y in data['args'].split('-') if y]
            process.extend(a)

        log.debug('Running {0}'.format(process))
        p = Popen(process)
        self._pid = p.pid
    
    def halt_process(self):
        log.debug('send terminate')
        Popen(['kill', str(self._pid)])

    def run(self):
        for item in self.pubsub.listen():
            log.debug('listen on queue')
            if self._pid != None:
                self.halt_process()

            if item['data'].upper() == 'KILL':
                log.debug('received kill message')
                self.pubsub.unsubscribe()
                break
            elif item['data'].upper() == 'STOP':
                pass
            else:
                self.start_process(item)

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
