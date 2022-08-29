from multiprocessing import Process, Queue

"""
研究思路：

    主进程和子进程之间借助于队列通信
    子进程和子进程之间借助于队列通信
    
"""


def producer(q):
    q.put('hello 001')
    print('one baby')


def consumer(q):
    print(q.get())


if __name__ == '__main__':
    q = Queue()
    p = Process(target=producer, args=(q,))
    p2 = Process(target=consumer, args=(q,))
    p.start()
    p2.start()
