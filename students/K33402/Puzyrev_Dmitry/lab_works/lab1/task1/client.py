from socket import *

conn = socket(AF_INET, SOCK_STREAM)
conn.connect(("127.0.0.1", 14900))

data = b"Hello, server!"
conn.send(data)

data = conn.recv(1024)
print(data.decode())

conn.close()
