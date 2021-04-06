import socket

if __name__ == '__main__':
    sock = socket.socket()
    sock.bind(('', 9090))
    sock.listen(1)
    conn, addr = sock.accept()

    conn.sendall(b'HTTP/1.0 200 OK\nContent-Type: text/html\n\n' + open('index.html', 'rb').read())

    conn.close()
