import socket


class Client:
    def __init__(self, port):
        self._socket = socket.socket(family=socket.AF_INET,
                                     type=socket.SOCK_STREAM,
                                     proto=0)
        self._socket.connect(('127.0.0.1', port))

    def send(self, height: int, width: int):
        print(f'YOU: height: {height}, width: {width}')
        self._socket.sendall(bytes(f'{height},{width}', 'utf-8'))
        data = self._socket.recv(1024)
        print(data.decode('utf-8'))
        self._socket.close()
        print('Connection closed')


if __name__ == '__main__':
    clint = Client(53331)
    clint.send(height=10, width=20)
