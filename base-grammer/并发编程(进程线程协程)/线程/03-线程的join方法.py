import time
from threading import Thread

money = 100


def task():
    print('线程启动')
    time.sleep(3)
    print('线程结束')


def task1():
    global money
    money = 666


if __name__ == '__main__':
    t1 = Thread(target=task)
    t2 = Thread(target=task1)
    t1.start()
    t2.start()

    print(money)
    t1.join()
    print('主线程结束')

# 线程之间的资源时共享的
