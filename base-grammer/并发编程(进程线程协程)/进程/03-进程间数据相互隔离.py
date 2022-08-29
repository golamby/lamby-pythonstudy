from multiprocessing import Process

money = 100


def task():
    global money
    money = 888
    print('子进程中的money', money)


if __name__ == '__main__':
    p1 = Process(target=task)
    p1.start()
    print('主进程中的money',money)