import time
from threading import Thread


def foo(name):
    print(f'{name} is running')
    time.sleep(1)
    print(f'{name} is over')


def task1():
    print('123')
    time.sleep(1)
    print('end123')


def task2():
    print('456')
    time.sleep(3)
    print('end456')


if __name__ == '__main__':
    t1 = Thread(target=task1, args=())
    t2 = Thread(target=task2, args=())
    t1.daemon = True
    # t2.daemon = True
    t1.start()
    t2.start()
    print('mainThread')
