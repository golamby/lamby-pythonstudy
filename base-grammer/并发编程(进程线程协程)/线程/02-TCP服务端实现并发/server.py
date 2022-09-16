import socket
from multiprocessing import Process
from threading import Thread

"""
    服务端基本的功能
    1.有固定的IP和端口
    2.24小时不停机
    3.支持并发
"""


# 链接循环

def talk(conn):
    # 通信循环
    while True:
        try:
            data = conn.recv(1024)
            if len(data) == 0: break
            print('客户端传来的信息', data)
            conn.send(data.upper())
        except ConnectionResetError as e:
            print(e)
            break
    conn.close()


def server(ip, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen(5)
    while True:
        conn, client_addr = server.accept()

        t = Thread(target=talk, args=(conn,))
        t.start()


if __name__ == '__main__':
    t = Thread(target=server, args=('127.0.0.1', 8808))
    t.start()
