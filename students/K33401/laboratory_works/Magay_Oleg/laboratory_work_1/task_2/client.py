import socket
import time

s = socket.socket()
s.connect(('localhost', 9090))
s.send('Hello, server'.encode("UTF-8"))

s = input().encode()
conn.send(s)

data = s.recv(1024)
s.close()

print(data.decode("UTF-8"))


