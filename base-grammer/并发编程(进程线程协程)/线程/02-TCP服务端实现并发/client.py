import socket

clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

clientSocket.connect(('127.0.0.1',8808))


while True:
    msg = input('向服务器发送信息').strip()
    if msg == 'quit':
        break
    if len(msg) == 0:
        continue
    clientSocket.send(msg)
    data = clientSocket.recv(1024)
    print('接收来自服务器的信息',data.decode('utf-8'))



clientSocket.close()




