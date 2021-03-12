import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("127.0.0.1", 14900))

print("Решение квадратного уравнения.\n Введите a b c через пробел:")
data = input()
conn.send(data.encode("utf-8"))

answer = conn.recv(16384)
print(answer.decode("utf-8"))

conn.close()