import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("localhost", 9090))
data = conn.recv(2048)
msg = data.decode("utf-8")
print(msg)
conn.close()
