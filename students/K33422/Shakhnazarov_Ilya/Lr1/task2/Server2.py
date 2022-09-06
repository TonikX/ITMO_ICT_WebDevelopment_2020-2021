import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(("localhost", 22001))
conn.listen(1)

while True:
    clientsocket, address = conn.accept()
    s = int(clientsocket.recv(1024).decode())
    h = int(clientsocket.recv(1024).decode())
    res = str(s*h)
    clientsocket.send(res.encode())
