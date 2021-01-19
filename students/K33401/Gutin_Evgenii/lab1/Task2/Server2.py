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
            print(f"{client_addr} has connected")

            while True:
                data = client_socket.recv(1024)
                if not data:
                    print(f"{client_addr} has disconnected")
                    break
                answer = Server.__compute(data.decode('utf-8'))
                client_socket.sendall(bytes(f'SERVER TO {client_addr}: S={answer}', 'utf-8'))
            client_socket.close()

    @staticmethod
    def __compute(data):
        data = data.split(',')
        return int(data[0]) * int(data[1])


if __name__ == '__main__':
    server = Server(53331, 1)
    server.run()
