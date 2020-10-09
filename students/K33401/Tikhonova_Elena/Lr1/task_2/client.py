import socket
import json

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

conn.connect(("127.0.0.1", 14900))
print(conn.recv(16384).decode("utf-8"))
a = float(input('Сторона параллелограмма: '))
a_h = float(input('Высота опущенная на эту сторону: '))
b = float(input('Другая сторона параллелограмма: '))
b_h = float(input('Высота опущенная на эту сторону: '))
alpha = float(input('Угол между сторонами: '))

paral_info = json.dumps(
    {'a': a, 'b': b, 'a_h': a_h, 'b_h': b_h, 'alpha': alpha})
conn.send(paral_info.encode("utf-8"))
print(conn.recv(16384).decode("utf-8"))
conn.close()