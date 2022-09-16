from threading import Thread, Event
import time

event = Event()


def light():
    print('红灯亮了,还剩三秒')
    time.sleep(3)
    print('绿灯亮了')
    # signal事件
    event.set()


def car(name):
    print(f'{name} 车在等红灯')
    event.wait()
    print(f'红灯结束，{name}车启动')


if __name__ == '__main__':
    t = Thread(target=light)
    t.start()

    for i in range(20):
        c = Thread(target=car, args=(f'car--{i}',))
        c.start()
