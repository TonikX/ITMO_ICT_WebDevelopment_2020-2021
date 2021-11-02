import socket
from math import sqrt

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 7777))
sock.listen(1)
conn, addr = sock.accept()

print('connected:', addr, conn)
d = ''
ch = ''
while True:
    conn.sendall(bytes(d + f'Нужно найти (a) - первый катет, (b) - второй катет , (c) - гипотенузу', "utf-8"))
    data = conn.recv(1024)
    ch = data.decode()

    if ch == 'a':
        conn.sendall(bytes(d + f'Введите значения гипотенузы и второго катета: ', "utf-8"))
        data = conn.recv(1024)
        print(data.decode())
        c, b = data.decode("utf-8").split(' ')
        a = sqrt((int(c) ** 2) - (int(b) ** 2))
        d = f'Первый катет равен = {a} \n'

    if ch == 'b':
        conn.sendall(bytes(d + f'Введите значения гипотенузы и первого катета: ', "utf-8"))
        data = conn.recv(1024)
        print(data.decode())
        c, a = data.decode("utf-8").split(' ')
        b = sqrt((int(c) ** 2) - (int(a) ** 2))
        d = f'Второй катет равен = {b} \n'

    if ch == 'c':
        conn.sendall(bytes(d + f'Введите значения первого катета и второго катета: ', "utf-8"))
        data = conn.recv(1024)
        print(data.decode())
        a, b = data.decode("utf-8").split(' ')
        c = sqrt((int(a) ** 2) + (int(b) ** 2))
        d = f'Гипотенуза равена = {c} \n'

    if not data:
        break
    sock.close()