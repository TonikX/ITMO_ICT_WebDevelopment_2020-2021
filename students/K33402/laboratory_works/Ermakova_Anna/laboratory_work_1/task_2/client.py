import socket

sock = socket.socket()
sock.connect(('localhost', 9090))
data = input('Введите значения оснований и высоты:\n')
sock.send(data.encode("utf-8"))
data = sock.recv(1024)
sock.close()

print(data.decode("utf-8"))
