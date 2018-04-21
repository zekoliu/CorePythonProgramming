import threading
from time import sleep, ctime   #使用可调用的类进行多线程

loops = [4,2]

def loop(nloop, nsec):
    print 'start loop', nloop, 'at:', ctime()
    sleep(nsec)
    print 'loop', nloop, 'done at:', ctime()
def main():
    print 'starting at:', ctime()
    threads = []
    nloop = range(len(loops))

    for i in nloop:
        t = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(t)

    for i in nloop:
        threads[i].start()

    for i in nloop:
        threads[i].join()

        print 'all DONE at:', ctime()

if __name__ == '__main__':
    main()