import socket


class Server:
    def __init__(self, port, clients):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        self.sock.bind(('localhost', port))
        self.sock.listen(clients)
    
    def run(self):
        while True:
            client_sock, client_addr = self.sock.accept()
            while True:
                data = client_sock.recv(4096)
                if not data:
                    print(f'{client_addr} has just lost connection')
                    break
                with open('index.html', 'r') as file:
                    html = file.read()
                    client_sock.sendall(bytes(f'HTTP/1.1 200 OK\nContent-Type: text/html\n\n{html}', 'utf-8'))

if __name__ == '__main__':
    serv = Server(12345, 1)
    serv.run()
