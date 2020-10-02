import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("127.0.0.1", 9090))
print("Введите длину основания и высоты через пробел:")
values = input()
values = values.encode('utf-8')
conn.send(values)

data = conn.recv(1024)
conn.close()

print(data.decode('utf-8'))