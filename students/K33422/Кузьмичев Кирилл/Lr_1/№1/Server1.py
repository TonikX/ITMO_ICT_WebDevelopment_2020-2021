import socket

Sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Sock.bind(("127.0.0.1", 11042))
Sock.listen(1)
conn, addr = Sock.accept()

while True:
    data = conn.recv(1024)
    if not data:
        break
    print(data.decode("utf-8"))
    conn.send(b'Hello back!')

conn.close()