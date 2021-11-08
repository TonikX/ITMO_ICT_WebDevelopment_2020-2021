import socket

Sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Sock.connect(("127.0.0.1", 11042))
Sock.send(b"Hello, server! \n")

data = Sock.recv(1024)
Sock.close()

print(data.decode("utf-8"))