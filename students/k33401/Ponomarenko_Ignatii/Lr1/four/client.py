import socket

sock = socket.socket()
sock.connect(('localhost', 9090))
while True:
	sock.send(input().encode("utf-8"))

data = sock.recv(1024)
sock.close()