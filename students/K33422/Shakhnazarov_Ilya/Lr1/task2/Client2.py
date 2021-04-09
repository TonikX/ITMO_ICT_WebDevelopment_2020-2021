import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("localhost", 22001))

s = input("основание = ")
h = input("высота = ")
conn.send(s.encode())
conn.send(h.encode())

data = conn.recv(1024)
print(data.decode())

conn.close()