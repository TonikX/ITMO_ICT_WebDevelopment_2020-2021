import socket


class Client:
    def __init__(self, port):
        self._socket = socket.socket(family=socket.AF_INET,
                                     type=socket.SOCK_STREAM,
                                     proto=0)
        self._socket.connect(('127.0.0.1', port))

    def send(self, message):
        print(f'You sent: {message}')
        self._socket.sendall(bytes(message, 'utf-8'))
        data = self._socket.recv(1024)
        print(f'From server got: {data.decode()}')
        self._socket.close()


if __name__ == '__main__':
    clint = Client(8088)
    clint.send('Hello, server!')
