import socket


class Client:
    def __init__(self, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        self.sock.connect(('localhost', port))

    def send(self, a, b, c):
        self.sock.sendall(bytes(f'{a} {b} {c}','utf-8'))
        data = self.sock.recv(1024)
        data.decode('utf-8')
        print(data)


if __name__ == '__main__':
    cl = Client(12345)
    cl.send(a=1, b=-8, c=12)
    cl.send(a=5, b=3, c=7)
    cl.send(a=1, b=-6, c=9)
