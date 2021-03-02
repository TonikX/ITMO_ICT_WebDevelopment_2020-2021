import socket


class Server:
    def __init__(self, port: int, clients: int):
        self._socket = socket.socket(family=socket.AF_INET,
                                     type=socket.SOCK_STREAM,
                                     proto=0)
        self._socket.bind(('127.0.0.1', port))
        self._socket.listen(clients)

    def run(self):
        while True:
            client_socket, client_addr = self._socket.accept()
            while True:
                data = client_socket.recv(1024)
                print(f'From {client_addr} got: {data.decode()}')
                client_socket.sendall(b'Hello client')
                client_socket.close()
                break


if __name__ == '__main__':
    server = Server(8088, 1)
    server.run()
