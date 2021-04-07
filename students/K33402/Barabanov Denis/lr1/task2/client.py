import socket

operation = 'pifagor'
sock = socket.socket()
sock.connect(('localhost', 9090))

sock.send(operation.encode())
data = sock.recv(1024)
print(data.decode())

sides = input()

sock.send(sides.encode())
data = sock.recv(1024)
sock.close()

print(data.decode())
