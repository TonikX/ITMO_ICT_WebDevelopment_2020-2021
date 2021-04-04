from socketserver import *
from math import sqrt

class MyTCPHandler(StreamRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024)
        leg1 = self.data.decode('utf-8').split()[0]
        leg2 = self.data.decode('utf-8').split()[1]
        hypotenuse = sqrt(float(leg1)**2+float(leg2)**2)

        #sendall - отправляет сообщение
        self.request.sendall(str(hypotenuse).encode('utf-8'))


if __name__ == "__main__":
    # создание экземпляра класса
    server = TCPServer(('localhost', 14900), MyTCPHandler)

    print('starting server.....')
    server.serve_forever()