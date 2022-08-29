import socketserver


# 链接循环，保证服务器一直保持运行，
# 客户端失去链接，关闭connection


class MyRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print(self.request)
        print(self.client_address)
        # 通信循环
        while True:
            try:
                data = self.request.recv(1024)
                # 针对unix系统，对于客户端意外关闭的状况
                if len(data) == 0:
                    break
                print('客户端发来消息', data)
                self.request.send(data.upper())
            except Exception:
                break

        self.request.close()


s = socketserver.ThreadingTCPServer(('127.0.0.1', 8089), MyRequestHandler)
s.serve_forever()

while True:

    conn, client_addr = serverSocket.accept()
    print(conn)
    print('客户端的ip和端口号', client_addr)



serverSocket.close()
