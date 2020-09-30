import socket

sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sckt.connect(('localhost', 8080))
sckt.sendall(b'Hello, server!')

data = sckt.recv(1024)
print(data.decode("utf-8"))

sckt.close()
