import socket

sock = socket.socket()
sock.connect(("localhost", 9000))
sock.send(b"Hello, server!")

data = sock.recv(1024)

print(data.decode("utf-8"))

sock.close()
