import time
from threading import Thread, Lock

money = 100
t_list = []
mutex = Lock()  # 锁机制


def task():
    global money
    temp = money
    time.sleep(0.1)
    money = temp - 1


def taskWithLock():
    global money
    mutex.acquire()
    temp = money
    time.sleep(0.1)
    money = temp - 1
    mutex.release()


if __name__ == '__main__':
    for i in range(100):
        t = Thread(target=taskWithLock)
        t_list.append(t)

    for t in t_list:
        t.start()
    for t in t_list:
        t.join()
    print(money)
