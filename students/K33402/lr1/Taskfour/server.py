import socket


class Server:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(('127.0.0.1', 14900))
        print('Start Server')

    def runServer(self):
        client = []
        while 1:
            data, addres = self.sock.recvfrom(1024)
            print(addres[0], addres[1])
            if addres not in client:
                client.append(addres)
            for clients in client:
                if clients == addres:
                    continue
                self.sock.sendto(data, clients)


if __name__ == '__main__':
    Server = Server()
    Server.runServer()
