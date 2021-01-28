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
                print(f'From {client_addr} got: {data}')
                if not data:
                    print(f"{client_addr} has disconnected")
                    break
                hypoten = Server.__find_hypotenuse(data.decode())
                client_socket.sendall(bytes(f'Hypotenuse/гипотенуза = {hypoten};', "UTF-8"))
            client_socket.close()

    @staticmethod
    def __find_hypotenuse(data):
        coefs = data.split(',')
        base = int(coefs[0])
        perpen = int(coefs[1])
        hypo = (base**2 + perpen**2)**0.5
        return hypo


if __name__ == '__main__':
    server = Server(8000, 1)
    server.run()
