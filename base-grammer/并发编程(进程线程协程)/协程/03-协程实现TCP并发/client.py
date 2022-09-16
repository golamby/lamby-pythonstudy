import socket
from threading import Thread, current_thread


def x_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 8748))
    n = 0
    while True:
        msg = input(f'{current_thread().name}发送{n}')
        n += 1
        client.send(msg.encode('utf-8'))
        data = client.recv(1024)
        print('从服务器接收的信息:', data.decode('utf-8'))

    client.close()


if __name__ == '__main__':
    for _ in range(500):
        t = Thread(target=x_client)
        t.start()
