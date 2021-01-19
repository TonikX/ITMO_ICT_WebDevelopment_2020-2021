from socket import *

conn = socket(AF_INET, SOCK_STREAM)
conn.connect(("127.0.0.1", 8000))

data = conn.recv(16384)
print(data.decode())

conn.close()
