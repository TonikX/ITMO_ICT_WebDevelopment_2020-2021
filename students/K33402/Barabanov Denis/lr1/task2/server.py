import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()
print(conn)
while True:
    data = conn.recv(1024)
    data = str(data.decode())
    print(data)
    if not data=='pifagor':
        conn.send('Такой задачи нет'.encode())
        break
    else:
        conn.send('введите катеты треугольника (a,b)'.encode())
        data = conn.recv(1024)
        data = str(data.decode())
        try:
            a, b = map(int, data.split(','))
        except:
            conn.send('неправильный ввоод'.encode())
        c = a**2 + b**2
        c = 'длина гипотенузы = '  + str(c**(1/2))
        conn.send(c.encode())

conn.close()