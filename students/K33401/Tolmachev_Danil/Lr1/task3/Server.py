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
                if not data:
                    break
                with open('Hello_world.html', 'r') as file:
                    html = file.read()
                    client_socket.sendall(bytes(f'HTTP/1.1 200 OK\nContent-Type: text/html\n\n{html}', 'utf-8'))
            client_socket.close()


if __name__ == '__main__':
    server = Server(8088, 1)
    server.run()
