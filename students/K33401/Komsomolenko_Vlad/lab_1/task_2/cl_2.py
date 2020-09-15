import socket
import time

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("127.0.0.1", 14900))
conn.send(b"Hello, server \n")
data = conn.recv(16384)
udata = data.decode("utf-8")
print(udata)
s = input().encode()
conn.send(s)
data = conn.recv(16384)
udata = data.decode("utf-8")
print("s = " + udata)
conn.close()