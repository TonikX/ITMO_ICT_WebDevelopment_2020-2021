import socket

if __name__ == '__main__':
    sock = socket.socket()
    sock.bind(('', 9090))
    sock.listen(1)
    conn, addr = sock.accept()

    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(data.decode("utf-8"))
        conn.send('Hello, client!'.encode("utf-8"))
    conn.close()
