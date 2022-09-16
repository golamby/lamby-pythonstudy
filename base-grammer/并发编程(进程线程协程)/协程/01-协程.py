import time
"""
    进程：拥有资源的基本单位
    线程：执行单位
    协程：这个概念是程序员创造出来的，并不存在，以代码的方式构建，------ 实际上就是单线程下的并发
    
    并发实际上就是多道技术的一个思想的体现
    多道技术--切换并保存状态
        一旦遇到IO,我们在代码级别完成切换
        这样cpu就好像没有经历IO一样，继续执行一些别的任务，提高效率
        
        
    切换的情况：
      IO密集型：  遇到IO，切换
      计算密集型： 程序长时间占用cpu切换
        
    我们在遇到计算密集型的任务时，往往使用多进程利用python的多核优势
    而在遇到IO密集型的任务时，往往使用多线程和协程的概念
    
    下面的func3 和 func4 就是实现协程的雏形，生成器generator
    generator 每次next方法都会运行直到遇到yield

"""




def func1():
    for i in range(10000000):
        i + 1


def func2():
    for i in range(10000000):
        i + 2


def func3():
    while True:
        10000000 + 1
        yield


def func4():
    g = func3()
    for i in range(10000000):
        10000000 + i
        next(g)


if __name__ == '__main__':
    start_time = time.time()
    # func2()
    # func1()
    func4()
    print(f'花费时间:{time.time() - start_time}')
