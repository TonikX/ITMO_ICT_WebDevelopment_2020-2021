import socket


def task3():
    sock = socket.socket()
    sock.bind(('', 33333))
    sock.listen(1)
    conn, _ = sock.accept()
    while True:
        data = conn.recv(1024)
        if not data:
            break
        with open('index.html', 'r') as file:
            html = file.read()
            conn.sendall(bytes(f'HTTP/1.0 200 OK\nContent-Type: text/html\n\n{html}', 'utf-8'))
    conn.close()


if __name__ == '__main__':
    task3()
