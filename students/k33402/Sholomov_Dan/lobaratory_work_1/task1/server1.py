import socket


def task1():
    sock = socket.socket()
    sock.bind(('', 11111))
    sock.listen(1)
    conn, _ = sock.accept()
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(data.decode('utf-8'))
        conn.send(bytes('Hello, client', "utf-8"))
    conn.close()


if __name__ == '__main__':
    task1()
