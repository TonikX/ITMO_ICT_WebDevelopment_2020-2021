import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 8080))
sock.sendall(b'Hello, server')

data = sock.recv(1024)
print(data.decode("utf-8"))

sock.close()