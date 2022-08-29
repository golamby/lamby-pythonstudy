import random
import time
from multiprocessing import Process, Queue,JoinableQueue


def producer(name, food, q):
    for i in range(10):
        data = f'{name}生产了{food}{i}'
        time.sleep(random.randint(1, 3))
        print(data)
        q.put(data)


def consumer(name, q):
    while True:
        food = q.get()
        # if food is None:
        #     break
        time.sleep(random.randint(1, 3))
        print(f'{name}吃了{food}')


if __name__ == '__main__':
    # q = Queue()
    q = JoinableQueue()
    p1 = Process(target=producer, args=('p1', '包子', q))
    p2 = Process(target=producer, args=('p2', '饺子', q))
    c1 = Process(target=consumer, args=('c1', q))
    c2 = Process(target=consumer, args=('c2', q))
    p1.start()
    p2.start()

    c1.daemon = True
    c2.daemon = True
    c1.start()
    c2.start()

    p1.join()
    p2.join()

    # q.put(None) 多少个消费者就需要多少个None，所以我们引入了JoinableQueue

    q.join()
