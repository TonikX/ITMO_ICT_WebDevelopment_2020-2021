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
        answer = Server.compute(data.decode('utf-8'))
        conn.send(bytes(f'SERVER TO {addr}: S={answer}', 'utf-8'))
        conn.close()

    def compute(data):
        data = data.split(',')
        return int(data[0]) * int(data[1])


if __name__ == '__main__':
    server = Server(14900)
    server.run()