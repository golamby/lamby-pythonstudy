import time
from multiprocessing import Process


def my_sleep(name, n):
    print(f'{name} is running')
    time.sleep(n)
    print(f'{name} is over')


def send_mes(num,start):
    time.sleep(num)
    print(f'{num}封邮件已经发送完毕')
    print(time.time() - start)


if __name__ == '__main__':
    # p1 = Process(target=my_sleep, args=('p1', 1))
    # p2 = Process(target=my_sleep, args=('p2', 2))
    # p3 = Process(target=my_sleep, args=('p3', 3))
    #
    # start_time = time.time()
    #
    # p1.start()
    # p2.start()
    # p3.start()
    # p1.join()
    # p2.join()
    # p3.join()
    #
    # print('主进程over', time.time() - start_time)
    start_time = time.time()
    p_list = []
    for i in range(1, 11):
        process = Process(target=send_mes, args=(i,start_time))
        process.start()
        p_list.append(process)

    for p in p_list:
        p.join()
    print('邮件发送完毕')
