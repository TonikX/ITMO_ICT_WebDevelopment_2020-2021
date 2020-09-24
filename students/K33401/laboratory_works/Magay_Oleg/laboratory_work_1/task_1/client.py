import socket

s = socket.socket()
s.connect(('localhost', 9090))
s.send('Hello, server'.encode("UTF-8"))

data = s.recv(1024)
s.close()

print(data.decode("UTF-8"))
