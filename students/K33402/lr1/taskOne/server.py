import socket


class Server:
    def __init__(self, port: int):
        self.sock = socket.socket()
        self.sock.bind(("", 14900))
        self.sock.listen(10)

    def run(self):
        conn, addr = self.sock.accept()
        data = conn.recv(16384)
        udata = data.decode("utf-8")
        print("Data: " + udata)
        conn.send(b"aaaaaaaaaaa!\n")
        conn.send(b"Your data: " + udata.encode("utf-8"))
        conn.close()


if __name__ == '__main__':
    server = Server(14900)
    server.run()
