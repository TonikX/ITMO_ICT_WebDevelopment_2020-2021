import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("127.0.0.1", 14902))
s = input("Введите основание: ")
h = input("Введите высоту: ")
conn.send(s.encode())
conn.send(h.encode())
data = conn.recv(1024)
print(data.decode())
conn.close()