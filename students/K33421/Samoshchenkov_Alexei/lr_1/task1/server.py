import socket


class Server:
    def __init__(self, port, clients):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        self.sock.bind(('localhost', port))
        self.sock.listen(clients)
    
    def run(self, message):
        while True:
            client_sock, client_addr = self.sock.accept()
            print(f'{client_addr} has just connected')
            while True:
                data = client_sock.recv(1024)
                if not data:
                    print(f'{client_addr} has just lost connection')
                    break
                client_sock.sendall(bytes(f'Server says "{message}" to {client_addr}', 'utf-8'))


if __name__ == '__main__':
    serv = Server(12345, 1)
    serv.run('Hello, Client')
