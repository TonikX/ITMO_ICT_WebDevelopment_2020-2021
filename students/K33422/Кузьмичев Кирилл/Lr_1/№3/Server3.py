import socket

Sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Sock.bind(("127.0.0.1", 11042))
Sock.listen(1)
conn, addr = Sock.accept()

while True:
    with open('index.html', 'r') as file:
        browse = file.read()
        conn.sendall(bytes(f'{browse}', 'utf-8'))
    data = conn.recv(1024)
    if not data:
        break

conn.close()