# from multiprocessing import Process, active_children, cpu_count
# import os
# import time
#
# print('执行了子进程导入')
#
#
# def task(name):
#     print(__name__)
#     print(f'{name} is running')
#     time.sleep(3)
#     print(f'{name} is over')
#
#
# """
#      申请内存空间，拷贝代码
#     windows中创建进程需要在main中创建，
#     因为windows中创建进程类似于模块的导入，是从上向下进行的
#     在Windows操作系统中由于没有fork(linux操作系统中创建进程的机制)，在创建子进程的时候会自动 import 启动它的这个文件，而在 import 的时候又执行了整个文件。
#     当start时会执行
# """
#
# if __name__ == '__main__':
#     p1 = Process(target=task, args=('t1',))
#     p2 = Process(target=task, args=('t2',))
#     p1.start()  # 向操作系统申请资源(内存空间，子进程pid号)，然后开始执行task任务，异步执行，本动作不影响主进程，主进程则会继续执行。
#     p2.start()
#     time.sleep(0.5)
#     print(active_children())
#     print(cpu_count())
#     print(os.cpu_count())


# 第二种方式创建多进程，继承方式
import os
import time
from multiprocessing import Process


def func(n):
    time.sleep(n)


class MyProcess(Process):

    def __init__(self, i,target):
        super(MyProcess,self).__init__()
        self.index = i
        self.target = target

    def run(self):
        self.target(self.index)
        print('子进程', self.index, os.getpid(), os.getppid())


if __name__ == '__main__':
    p_list = []
    for i in range(10):
        process = MyProcess(i,func)
        process.start()
        p_list.append(process)

    for p in p_list:
        p.join()
    print('主进程，', os.getpid())
