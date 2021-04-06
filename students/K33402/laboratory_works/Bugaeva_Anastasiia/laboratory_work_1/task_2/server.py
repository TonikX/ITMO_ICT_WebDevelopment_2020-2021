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
        a, h = data.decode("utf-8").split()
        conn.send(('Answer: ' + str(float(a) * float(h))).encode("utf-8"))
    conn.close()
