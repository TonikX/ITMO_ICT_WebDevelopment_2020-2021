import socket

class Client:
    def __init__(self, port: int):
        self.conn = socket.socket()
        self.conn.connect(("127.0.1.1", port))


    def work(self, height:int, width:int):
        self.conn.sendall(bytes(f'{height},{width}', 'utf-8'))
        data = b""
        tmp = self.conn.recv(1024)
        while tmp:
            data += tmp
            tmp = self.conn.recv(1024)
        print(data.decode("utf-8"))
        self.conn.close()

if __name__ == '__main__':
    clint = Client(14900)
    clint.work(23, 32)