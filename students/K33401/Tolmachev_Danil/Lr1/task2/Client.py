import socket


class Client:
    def __init__(self, port):
        self._socket = socket.socket(family=socket.AF_INET,
                                     type=socket.SOCK_STREAM,
                                     proto=0)
        self._socket.connect(('127.0.0.1', port))

    def send(self, a: int, b: int, c: int):
        self._socket.sendall(bytes(f'{a},{b},{c}', 'utf-8'))
        data = self._socket.recv(1024)
        print(data.decode('utf-8'))

    def close(self):
        self._socket.close()


if __name__ == '__main__':
    clint = Client(8000)
    clint.send(3, -14, -5)
    clint.send(3, -18, 27)
    clint.close()

