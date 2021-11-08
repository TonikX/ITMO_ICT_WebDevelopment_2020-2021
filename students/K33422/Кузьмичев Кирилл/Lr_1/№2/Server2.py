import socket
from math import sqrt

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 8888))
sock.listen(1)
conn, addr = sock.accept()

print('connected:', addr, conn)
d = ''
option = ''
while True:
    conn.sendall(bytes(d + f'Каким способом хотите найти площадь трапеции: \n (a) - Через основания и высоту, (b) - Через среднюю линию и высоту', "utf-8"))
    data = conn.recv(1024)
    option = data.decode()

    if option == 'a':
        conn.sendall(bytes(d + f'Введите значения двух оснований(a, b) и высоты(h): ', "utf-8"))
        data = conn.recv(1024)
        print(data.decode())
        a, b, h = data.decode("utf-8").split(' ')
        S = (int(h) * (int(a)+int(b)))/2
        d = f'Площадь равна = {S} \n'

    if option == 'b':
        conn.sendall(bytes(d + f'Введите значения средней линии(m) и высоты(h): ', "utf-8"))
        data = conn.recv(1024)
        print(data.decode())
        m, h = data.decode("utf-8").split(' ')
        S = int(m) * int(h)
        d = f'Площадь равна = {S} \n'

    if not data:
        break
    sock.close()