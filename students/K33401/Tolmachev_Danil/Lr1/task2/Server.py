import socket
import math


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
                print(f'From {client_addr} got: {data}')
                if not data:
                    print(f"{client_addr} has disconnected")
                    break
                x1, x2 = Server.__resolve_equation(data.decode())
                client_socket.sendall(bytes(f'x1 = {x1}; x2 = {x2}', "UTF-8"))
            client_socket.close()

    @staticmethod
    def __resolve_equation(data):
        coefs = data.split(',')
        a = int(coefs[0])
        b = int(coefs[1])
        c = int(coefs[2])
        discr = b ** 2 - 4 * a * c
        if discr > 0:
            x1 = (-b + math.sqrt(discr)) / (2 * a)
            x2 = (-b - math.sqrt(discr)) / (2 * a)
            return x1, x2
        elif discr == 0:
            x = -b / (2 * a)
            return x, x
        else:
            return None, None


if __name__ == '__main__':
    server = Server(8000, 1)
    server.run()
