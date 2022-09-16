import time
from threading import Thread, current_thread, active_count
import os


def task(n):
    # print('当前线程进程号', os.getpid())
    print('线程名字', current_thread().name)
    time.sleep(n)


if __name__ == '__main__':
    t1 = Thread(target=task, args=(1,))
    t2 = Thread(target=task, args=(2,))
    t1.start()
    t2.start()
    t2.join()
    print('活跃线程数', active_count())
    # print('主线程的进程号',os.getpid())
    print('主线程的名字', current_thread().name)
