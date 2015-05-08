#! /usr/bin/env python3

import threading
from queue import Queue
import time

lock = threading.Lock()


def do_work_for_big_task(item):
    time.sleep(1)
    with lock:
        print(threading.current_thread().name, item)


def worker():
    while True:
        item = q.get()
        do_work_for_big_task(item)
        q.task_done()


if __name__ == '__main__':

    q = Queue()

    for i in range(100):
        t = threading.Thread(target=worker)
        t.daemon = True
        t.start()


    start  = time.perf_counter()

    for item in range(1000):
        q.put(item)

    q.join()

    print('time:', time.perf_counter() - start)
