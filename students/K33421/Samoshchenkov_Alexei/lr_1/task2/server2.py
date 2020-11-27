import socket
import math


class Server:
    def __init__(self, port, clients):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        self.sock.bind(('localhost', port))
        self.sock.listen(clients)
    
    def run(self):
        while True:
            client_sock, client_addr = self.sock.accept()
            while True:
                data = client_sock.recv(1024)
                if not data:
                    print(f'{client_addr} has just lost connection')
                    break
                data.decode('utf-8')
                x1, x2 = Server.solve(data)
                client_sock.sendall(bytes(f'x1 = {x1}"; x2 = {x2}', 'utf-8'))

    @staticmethod
    def solve(data):
        coef = data.split()
        a = int(coef[0])
        b = int(coef[1])
        c = int(coef[2])
        D = b**2-4*a*c
        if D>0:
            x1 = (-b+math.sqrt(D))/(2*a)
            x2 = (-b-math.sqrt(D))/(2*a)
            return x1, x2
        elif D==0:
            x1 = -b/(2*a)
            return x1, None
        else:
            return None, None

if __name__ == '__main__':
    serv = Server(12345, 1)
    serv.run()
