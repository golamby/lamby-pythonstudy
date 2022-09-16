import time
from threading import Thread


# from multiprocessing import Process
#
#
# def task(name):
#     print(f'{name} is running')
#     time.sleep(1)
#     print(f'{name} is over')
#
#
# t = Thread(target=task, args=('t1',))
# t.start()


# if __name__ == '__main__':
#     p = Process(target=task,args=('p1',))
#     p.start()

class MyThread(Thread):
    def __init__(self, name):
        super(MyThread, self).__init__()
        self.name = name

    def run(self):
        print(f'{self.name} is running')
        time.sleep(1)
        print(f'{self.name} is over')


if __name__ == '__main__':
    t1 = MyThread('t1')
    t1.start()
    print('主线程结束')
