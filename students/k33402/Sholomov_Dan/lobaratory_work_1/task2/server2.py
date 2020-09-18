import socket


def task2():
    sock = socket.socket()
    sock.bind(('', 22222))
    sock.listen(1)
    conn, _ = sock.accept()
    while True:
        data = conn.recv(1024)
        if not data:
            break
        inp = data.decode('utf-8').split()
        if len(inp) != 2:
            conn.send(bytes('Неверный формат ввода', "utf-8"))
            break
        conn.send(bytes(str(int(inp[0])*int(inp[1])), "utf-8"))
    conn.close()


if __name__ == '__main__':
    task2()
