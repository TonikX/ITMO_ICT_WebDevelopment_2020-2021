import socket

class Client:
    def __init__(self, port):
        self._socket = socket.socket(family=socket.AF_INET,
                                     type=socket.SOCK_STREAM,
                                     proto=0)
        self._socket.connect(('127.0.0.1', port))

    def send(self, a: int, b: int):
        self._socket.sendall(bytes(f'{a},{b}', 'utf-8'))
        data = self._socket.recv(1024)
        print(data.decode('utf-8'))

    def close(self):
        self._socket.close()

if __name__ == '__main__':
    my_client = Client(8000)
    my_client.send(3, 4)
    my_client.send(6, 8)
    my_client.close()

