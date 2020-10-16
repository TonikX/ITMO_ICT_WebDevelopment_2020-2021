import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(("127.0.0.1", 14902))
conn.listen(1)

while True:
    conn, addr = sock.accept()
    data = conn.recv(1024)
    if not data:
        break
    conn.sendall(b'HTTP/1.0 200 OK\r\nContent-Type: text/html\r\n\r\n' + open('index.html', 'rb').read())
    conn.close()