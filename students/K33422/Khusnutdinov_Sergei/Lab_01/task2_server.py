import socket
from math import sqrt

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', 9090))
server.listen(1)
conn, addr = server.accept()

print('Connected: ', addr)

while True:
	try:
		data = conn.recv(1024)
		if not data:
			break
		a, b, c = data.decode('utf-8').split(' ')
		a = int(a)
		b = int(b)
		c = int(c)
		D = b*b - 4*a*c
		if D > 0:
			x1 = (-b + sqrt(D))/(2*a)
			x2 = (-b - sqrt(D))/(2*a)
			conn.send("x1: {}, x2: {}".format(int(x1), int(x2)).encode('utf-8'))
		elif D == 0:
			x = (-b + sqrt(D))/(2*a)
			conn.send("x: {}".format(int(x)).encode('utf-8'))
		else:
			conn.send("There is no roots (D < 0)".encode('utf-8'))
	except KeyboardInterrupt:
		server.close()
		break