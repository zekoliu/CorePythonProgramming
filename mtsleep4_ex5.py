
import threading
from myThread import MyThread
from time import sleep, ctime

loops = (4, 2)

class ThreadFunc(object):

    def __init__(self, func, args, name = ''):
        self.name = name
        self.func = func
        self.args = args

    def run(self):
        apply(self.func, self.args)

    def loop(nloop, nsec):
        print 'start loop', nloop, 'at: ', ctime()
        sleep(nsec)
        print 'loop', nloop, 'done at: ', ctime()

    def main():
        print 'starting at: ', ctime()
        threads = []
        nloops = range(len(loops))

        for i in nloops:
            t = MyThread(loop, (i, loops[i]), loop)