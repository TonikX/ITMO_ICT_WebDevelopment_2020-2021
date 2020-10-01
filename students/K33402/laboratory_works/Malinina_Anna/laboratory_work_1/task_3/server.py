import socket

if __name__ == '__main__':
    sock = socket.socket()
    sock.bind(('', 9090))
    sock.listen(1)
    while True:
        conn, addr = sock.accept()
        data = conn.recv(1024)
        if not data:
            break
        conn.sendall(b'HTTP/1.0 200 OK\r\nContent-Type: text/html\r\n\r\n' + open('index.html', 'rb').read())
        conn.close()
