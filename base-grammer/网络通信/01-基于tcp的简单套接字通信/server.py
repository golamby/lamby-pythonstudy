import socket
import socketserver

# 创建一个套接字
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定服务端ip和端口
serverSocket.bind(('127.0.0.1', 8088))

serverSocket.listen(5)  # 半连接池

# 接收连接
conn, client_addr = serverSocket.accept()
print(conn)
print('客户端的ip和端口号', client_addr)

# 通信
data = conn.recv(1024)
print('客户端发来消息', data)
conn.send(data.upper())

# 关闭与客户端连接
conn.close()

# （可选）关闭服务端套接字
serverSocket.close()
