import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 7777))
s.send(b"Hello, server! \n")

data = s.recv(1024)
s.close()

print(data.decode("utf-8"))