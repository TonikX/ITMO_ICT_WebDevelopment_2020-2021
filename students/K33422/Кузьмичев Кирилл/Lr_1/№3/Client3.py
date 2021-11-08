import socket

Sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Sock.connect(("127.0.0.3", 11042))
Sock.send('Hello, server!'.encode("utf-8"))

data = Sock.recv(1024)
Sock.close()

print(data.decode("utf-8"))