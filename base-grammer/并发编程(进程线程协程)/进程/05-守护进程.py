# 主进程创建守护进程
# 1：守护进程会在主进程代码执行结束后就终止
# 2：守护进程内无法再开启子进程,否则抛出异常：AssertionError: daemonic processes are not allowed to have children
# 注意：进程之间是互相独立的，主进程代码运行结束，守护进程随即终止


from multiprocessing import Process
import time


#
#
# def func():
#     print('子进程 start')
#     time.sleep(8)
#     print('子进程 over')
#
#
# if __name__ == '__main__':
#     p = Process(target=func)
#     p.daemon = True
#     p.start()
#
#     time.sleep(5)  # 主进程休眠五秒后代码执行完毕
#     print('主进程结束')


# 守护进程会在主进程代码执行结束后就终止 ，但是父进程会等待子进程结束才正式结束。
# 注意：代码结束是指代码运行到了最后一行，并不代表进程已经结束了。

# def func():
#     count = 1
#     while True:
#         print(count * '*')
#         time.sleep(1)
#         count += 1
#
#
# def func2():
#     print('p2 start')
#     time.sleep(5)
#     print('p2 over')
#
#
# if __name__ == '__main__':
#     p1 = Process(target=func)
#     p1.daemon = True
#     p1.start()
#
#     Process(target=func2).start()
#     time.sleep(3)
#     print('主进程执行完毕')


# 3，守护进程的作用
# 守护进程可以报活，就是向某个服务报告自己还活着

# 场景：
# 例如你写好了一个网页，你的服务端是不应该停的，因为你服务端一旦停止了，别人就无法访问你的网页了，所以我们应该确保服务端没有‘死’，
# 这个时候就可以使用守护进程，在你的服务端起一个守护进程，让这个进程只做一件事，就是每隔1个小时(时间按照自己的合理安排设定)向某一台机器汇报自己还活着，
# 一旦这个机器没有收到你守护进程传来的消息，那么就可以认为你的服务端已经挂了。
#
# 例如：
import time
from multiprocessing import Process
def Guard():
    while True:
        time.sleep(3600)
        print('我还活着') # 向某个机器汇报我还活着，具体该怎么写汇报的逻辑就怎么写，这里只是示范

if __name__ == '__main__':
    p = Process(target=Guard)
    p.daemon = True
    p.start()
    # 主进程的逻辑(主进程应该是一直运行的，不应该有代码结束的时候)
    print('主进程')