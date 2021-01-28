import socket


class Client:
    def __init__(self, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        self.sock.connect(('localhost', port))

    def send(self, message):
        print(f'{message}')
        self.sock.sendall(bytes(f'{message}','utf-8'))
        data = self.sock.recv(1024)
        data.decode('utf-8')
        print(data)
        self.sock.close()


if __name__ == '__main__':
    cl = Client(12345)
    cl.send('Hello, server')
