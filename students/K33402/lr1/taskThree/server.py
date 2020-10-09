import socket


class Server:
    def __init__(self, port: int):
        self.sock = socket.socket()
        self.sock.bind(("", 14900))
        self.sock.listen(10)

    def work(self):
        while True:
            conn, addr = self.sock.accept()
            print(f"{addr} has connected")
            data = conn.recv(16384)
            if not data:
                print(f"{addr} has disconnected")
                break
            with open('index.html', 'r') as file:
                html = file.read()
                conn.send(bytes(f'HTTP/1.0 200 OK\nContent-Type: text/html\n\n{html}', 'utf-8'))
        conn.close()




if __name__ == '__main__':
    server = Server(14900)
    server.work()