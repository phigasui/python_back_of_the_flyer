#! /usr/local/bin/python3

from multiprocessing import Process, Queue
import os
import time


def info(title):
    print(title)
    print('module name:', __name__)
    if hasattr(os, 'getppid'):
        print('parent process:', os.getppid())
    print('process id:', os.getppid())
    
        
def f(name):
    info('function f')
    time.sleep(3)
    print('hello', name)

    
def g(name):
    info('function g')
    time.sleep(3)
    print('hello', name)


def wait(number, q):
    print('s', number)
    time.sleep(3)
    # return number + 10
    q.put(number)

if __name__ == '__main__':
    # info('main line')
    # p1 = Process(target=f, args=('bob', ))
    # p2 = Process(target=f, args=('john', ))
    # p1.start()
    # p2.start()
    # p1.join()
    # p2.join()

    # arg_list = [i for i in range()]
    
    # p = Pool()

    queues = [Queue() for i in range(30)]
    
    print("start")

    # result_list = p.map(wait, arg_list)

    processes = [Process(target=wait, args=(i, queues[i],)) for i in range(30)]

    # print(result_list)

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    for q in queues:
        print('e', q.get())
