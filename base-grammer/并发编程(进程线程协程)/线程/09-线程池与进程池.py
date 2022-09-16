import os
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time

# 不传参数，会开设cpu个数5倍的线程
tpool = ThreadPoolExecutor(5)

# 不传参数，默认是cpu个数个进程
ppool = ProcessPoolExecutor(5)


def task(n):
    print(n, os.getpid())
    time.sleep(2)
    return n * n


'''
任务提交的方式：
    1.同步
    2.异步
'''


# # 这里任务的提交是异步的
# res = pool.submit(task, 1)
# print(res)  # <Future at 0x21ebdcff048 state=running>
# print(res.result())
# print('主线程结束')


# 回调机制
def callback(n):
    print('call_back >>>', n.result())


if __name__ == '__main__':
    t_list = []
    for i in range(20):
        res = ppool.submit(task, i).add_done_callback(callback)
        t_list.append(res)

    # ppool.shutdown()
    # for t in t_list:
    #     print(t.result())
