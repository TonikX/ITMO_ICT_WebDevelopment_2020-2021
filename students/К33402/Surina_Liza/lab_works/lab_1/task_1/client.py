import socket

conn = socket.socket()
conn.connect(('localhost', 9090))
conn.send(b"Hello, server. \n")

data = conn.recv(1024)
msg = data.decode("utf-8")
print("Server: " + msg)

conn.close()
