import json
import time
from multiprocessing import Process, Lock


def search(i):
    with open(r'06-data.json', mode='rt', encoding='utf-8') as f:
        ticket_info = json.load(f)
    print(f'用户%s余票查询剩余%s' % (i, ticket_info.get('ticket_count')))


def buy(i):
    with open(r'06-data.json', mode='rt', encoding='utf-8') as f:
        ticket_info = json.load(f)
    time.sleep(0.2)
    if ticket_info.get('ticket_count', 0) > 0:
        ticket_info['ticket_count'] -= 1
        with open('06-data.json', mode='wt', encoding='utf-8') as f:
            json.dump(ticket_info, f)
            time.sleep(0.2)
        print('用户%s购票成功' % i)
    else:
        print('用户%s购买失败，无余票' % i)


def runWithNoLock(i):
    search(i)
    buy(i)


def runWithLock(i, lock):
    search(i)
    lock.acquire()
    buy(i)
    lock.release()


if __name__ == '__main__':

    # for i in range(5):
    #     process = Process(target=runWithNoLock, args=(i,))
    #     process.start()
    lock = Lock()
    for i in range(5):
        process = Process(target=runWithLock, args=(i, lock))
        process.start()
