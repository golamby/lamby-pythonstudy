import socket
import socketserver

# 创建一个套接字
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientSocket.connect(('127.0.0.1', 8088))
while True:
    msg = input('请输入向服务器发送的内容').strip()
    if msg == 'quit':
        break
    if len(msg) == 0:
        continue
    clientSocket.send(msg.encode('utf-8'))
    data = clientSocket.recv(1024)
    print(data.decode('utf-8'))

# 必选的，关闭资源
clientSocket.close()
