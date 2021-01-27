import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 8080))
sock.listen(1)
clientsoc, addr = sock.accept()
print('connected:', addr)
message = ''

while True:
    clientsoc.sendall(bytes(message + 'Впишите значения двух оснований и высоты трапеции:', "utf-8"))
    try:
        data = clientsoc.recv(1024)
        if not data:
            break
        if data.decode("utf-8") == "end":
            clientsoc.close()
            break
        a, b, h = data.decode("utf-8").split(' ')
        s = 0.5 * (int(a) + int(b)) * int(h)
        message = f'Площадь трапеции: {s}; \n'
    except KeyboardInterrupt:
        clientsoc.close()
        break
