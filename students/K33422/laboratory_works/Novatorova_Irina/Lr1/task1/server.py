from socketserver import *

class MyTCPHandler(StreamRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024)
        print('client send: '+str(self.data.decode('utf-8')))

        #sendall - отправляет сообщение
        self.request.sendall('Hello from server!'.encode('utf-8'))


if __name__ == "__main__":
    # создание экземпляра класса
    server = TCPServer(('localhost', 14900), MyTCPHandler)

    print('starting server.....')
    server.serve_forever()