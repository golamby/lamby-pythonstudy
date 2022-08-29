import socket
import socketserver

# 创建一个套接字
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverSocket.bind(('127.0.0.1', 8088))

serverSocket.listen(5)

conn, client_addr = serverSocket.accept()
print(conn)
print('客户端的ip和端口号', client_addr)

while True:
    try:
        data = conn.recv(1024)
        # 针对unix系统，对于客户端意外关闭的状况
        if len(data) == 0:
            break
        print('客户端发来消息', data)
        conn.send(data.upper())
    except Exception:
        break

conn.close()

serverSocket.close()
