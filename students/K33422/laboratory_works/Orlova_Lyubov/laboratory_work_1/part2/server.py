import socket
import math

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()
print('connected:', addr)

conn.send(bytes(" Введите a: ", "utf-8"))
a = conn.recv(1024)
print(a.decode("utf-8"))

conn.send(bytes(" Введите b: ", "utf-8"))
b = conn.recv(1024)
print(b.decode("utf-8"))

conn.send(bytes(" Введите c: ", "utf-8"))
c = conn.recv(1024)
print(c.decode("utf-8"))

a = int(a)
b = int(b)
c = int(c)

D = b * b - 4 * a * c

if D < 0 :
    conn.send(bytes("Корней нет(D < 0)", "utf-8"))
else:
    x1 = str((- b + math.sqrt(D)) / ( 2 * a ))
    x2 = str((- b - math.sqrt(D)) / ( 2 * a ))
    print(x1)
    print(x2)
    conn.send(bytes("Ответ: x1 = %s, x2 = %s" % (x1, x2), "utf-8"))

conn.close()
