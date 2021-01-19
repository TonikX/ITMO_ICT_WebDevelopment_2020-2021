import socket


class Server:
    def __init__(self, port: int, clients: int):
        self._socket = socket.socket(family=socket.AF_INET,
                                     type=socket.SOCK_STREAM,
                                     proto=0)
        self._socket.bind(('127.0.0.1', port))
        self._socket.listen(clients)

    def run(self, message):
        while True:
            client_socket, client_addr = self._socket.accept()
            print(f"{client_addr} has connected")

            while True:
                data = client_socket.recv(1024)
                if not data:
                    print(f"{client_addr} has disconnected")
                    break
                client_socket.sendall(bytes(f'SERVER TO {client_addr}: {message}', 'utf-8'))
            client_socket.close()


if __name__ == '__main__':
    server = Server(53330, 1)
    server.run('Nothing, just chilling, killing..')
