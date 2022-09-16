from threading import Thread, Semaphore
import random
import time

sm = Semaphore(5)


def func(name):
    sm.acquire()
    print(f'{name} is using toilet')
    time.sleep(random.randint(1, 5))
    print(f'{name} has done')
    sm.release()


if __name__ == '__main__':
    for i in range(20):
        t = Thread(target=func, args=(f'person--{i}',))
        t.start()
