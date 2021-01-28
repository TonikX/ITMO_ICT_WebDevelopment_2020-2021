import socket

host = "127.0.0.1"
port = 9091

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.send(b"Hello, server \n")

data = s.recv(16384)
print( data.decode("utf-8"))

s.close()