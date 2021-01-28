import socket

sock = socket.socket()
sock.connect(("localhost", 9000))

sides = input("Input lengths of sides: a b ")

sock.send(sides.encode("UTF-8"))
data = sock.recv(1024)
print(data.decode("UTF-8"))
sock.close()