import redis
import threading
import time
import os
import logging
from subprocess import Popen
import signal
import json
import random


class Listener(threading.Thread):
    def __init__(self, r, channels):
        threading.Thread.__init__(self)
        self.redis = r
        self.pubsub = self.redis.pubsub(ignore_subscribe_messages = True)
        self.pubsub.subscribe(channels)
        self._pid = None
        self._show_random = False
        self._animations = [
            'mario.py', 'kit.py', 'scanning-pixel.py', 'rotating-block-generator.py',
            'gol-acorn.py', 'gol-block-switch.py', 'gol-gosper-gun.py', 'gol-pent.py', 'gol-red-glider.py',
            'spaceInvader.py'
        ]

    def start_process(self, item):
        data = json.loads(item['data'])
        args = None
        className = '{0}'.format(data['moduleName'])
        path = os.path.abspath('animation/{}'.format(className))
        process = ['python', path, '--led-no-hardware-pulse', '1', '-r', '32', '--led-chain', '2', '--led-multiplexing', '1', '--led-cols', '64', '--led-gpio-mapping', 'adafruit-hat']
        if 'args' in data.keys() and data['args']:
            a = ['-{0}'.format(y) for y in data['args'].split('-') if y]
            process.extend(a)

        log.debug('Running {0}'.format(process))
        p = Popen(process)
        self._pid = p.pid
 
    def start_gif(self):
        self._show_random = not self._show_random
        if not self._show_random:
            item = {"moduleName": "runtext.py"}
            self.start_process({"data": json.dumps(item)})
            return 

        files = os.listdir("/home/pi/gifs")
        image_path = "/home/pi/gifs/{0}".format(random.choice(files))
        process = [
                'led-image-viewer', '--led-multiplexing=1', '--led-chain=2', '--led-cols=32', 
                '--led-no-hardware-pulse', '--led-rows=32', '--led-gpio-mapping=adafruit-hat', 
                '--led-brightness=35', '-C', image_path
        ]
        log.debug('Running {0}'.format(process))
        p = Popen(process)
        self._pid = p.pid
        process = ["python", "stop_after_twenty.py"]
        Popen(process)

    def halt_process(self):
        log.debug('send terminate')
        Popen(['kill', str(self._pid)])

    def start_random_gol(self):
        self._show_random = not self._show_random
        if self._show_random:
            item = {"moduleName": "gol-random.py"}
            self.start_process({"data": json.dumps(item)})
            return

        item = {"moduleName": "runtext.py"}
        self.start_process({"data": json.dumps(item)})

    def start_random(self):
        self._show_random = not self._show_random
        if self._show_random:
            item = {"moduleName": random.choice(self._animations)}
            self.start_process({"data": json.dumps(item)})
            process = ["python", "stop_after_twenty.py"]
            Popen(process)
            return

        item = {"moduleName": "runtext.py"}
        self.start_process({"data": json.dumps(item)})

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
               # self.start_random() 
               # self.start_gif()
               self.start_random_gol()
            else:
                self.start_gif()
                # self.start_process(item)

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
