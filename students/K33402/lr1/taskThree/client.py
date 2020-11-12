import socket

class Client:
    def __init__(self, port: int):
        self.conn = socket.socket()
        self.conn.connect(("127.0.1.1", port))


    def work(self):
        self.conn.send(bytes(f'.', 'utf-8'))
        data = self.conn.recv(2048)
        print(data.decode("utf-8"))
        self.conn.close()

if __name__ == '__main__':
    clint = Client(14900)
    clint.work()