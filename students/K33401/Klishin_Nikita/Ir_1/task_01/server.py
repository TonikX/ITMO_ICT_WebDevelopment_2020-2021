import socketserver


class MyTCPHandler(socketserver.StreamRequestHandler):

    # обработчик входящих соединений
    def handle(self):
        self.data = self.request.recv(1024)
        value = bytes.decode(self.data)
        print("CLIENT SEND: " + value)

        self.request.sendall(b"Hello, client")

if __name__ == "__main__":
    # создание сервера
    server = socketserver.TCPServer(("127.0.0.1", 3000), MyTCPHandler)

    print("Starting TCP server...")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("Stopping server...")