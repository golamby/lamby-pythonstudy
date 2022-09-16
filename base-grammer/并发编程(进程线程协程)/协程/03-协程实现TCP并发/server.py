import socket
from threading import Thread
from gevent import spawn
from gevent import monkey;

monkey.patch_all()


def talk(conn):
    while True:
        try:
            data = conn.recv(1024)
            if len(data) == 0:
                break
            print('客户端的信息：', data)
            conn.send(data.upper())
        except ConnectionResetError as e:
            print(e)
    conn.close()


def server(ip, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen(5)

    while True:
        conn, client_addr = server.accept()
        spawn(talk, conn)
        # t = Thread(target=talk, args=(conn,))
        # t.start()


if __name__ == '__main__':
    g1 = spawn(server, *('127.0.0.1', 8748))
    g1.join()

    # Thread(target=server, args=('127.0.0.1', 8748)).start()
