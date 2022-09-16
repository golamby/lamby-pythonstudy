from gevent import monkey;monkey.patch_all()
from gevent import spawn

import time


def he():
    print('hehe')
    time.sleep(3)
    print('hehe')


def ha():
    print('haha')
    time.sleep(2)
    print('haha')


if __name__ == '__main__':
    start_time = time.time()
    g1 = spawn(he)
    g2 = spawn(ha)
    g1.join()
    g2.join()
    # he()
    # ha()
    # print(f'总耗时:{time.time() - start_time}s')  # 总耗时:5.048069953918457s
    print(f'总耗时:{time.time() - start_time}s')  # 总耗时:3.032947063446045s
