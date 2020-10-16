import socket

sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sckt.bind(('localhost', 8080))
sckt.listen(1)

while True:
    clientsocket, address = sckt.accept()
    clientsocket.sendall(bytes(f'Введите основание и высоту', "utf-8"))
    try:
        data = clientsocket.recv(1024)
        if not data:
            break
        a, h = data.decode("utf-8").split(' ')
        s = int(a) * int(h)
        clientsocket.sendall(bytes(f'Площадь параллелограмма {s}', "utf-8"))

    except KeyboardInterrupt:
        clientsocket.close()
        break
