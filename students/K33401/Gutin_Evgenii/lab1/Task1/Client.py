import socket


class Client:
    def __init__(self, port):
        self._socket = socket.socket(family=socket.AF_INET,
                                     type=socket.SOCK_STREAM,
                                     proto=0)
        self._socket.connect(('127.0.0.1', port))

    def send(self, message):
        print(f'YOU: {message}')
        self._socket.sendall(bytes(f'{message}', 'utf-8'))
        data = self._socket.recv(1024)
        print(data.decode('utf-8'))
        self._socket.close()
        print('Connection closed')


if __name__ == '__main__':
    clint = Client(53330)
    clint.send('Whatcha doing?')
