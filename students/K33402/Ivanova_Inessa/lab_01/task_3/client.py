import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("127.0.0.1", 14902))
data = conn.recv(1024)
print(data.decode())
conn.close()