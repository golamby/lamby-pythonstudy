from multiprocessing import Process, current_process
import time
import os


def task():
    print('子进程 :%s is running' % current_process().pid)  # 查看当前进程的进程号
    print('子进程 :%s is running' % os.getpid())  # 查看当前进程的进程号
    print(f'查看父进程的pid:{os.getppid()}')
    time.sleep(2)


if __name__ == '__main__':
    p1 = Process(target=task)
    p1.start()
    # p1.terminate()
    # time.sleep(0.5)  # 给is_alive方法反应时间
    # print(p1.is_alive())
    time.sleep(1)
    print('主进程 %s over ' % current_process().pid)
