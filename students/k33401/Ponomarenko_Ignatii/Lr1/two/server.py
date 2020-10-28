import socket

sock = socket.socket()
sock.bind(('localhost', 9090))
sock.listen(1)

while True:
	try:
		conn, addr = sock.accept()
		data = conn.recv(1024)
		S = data.decode('utf-8')
		a, b = map(float, S.split())
		c = str((a**2 + b**2)**0.5)
		conn.send(c.encode("utf-8"))
	except KeyboardInterrupt:
		conn.close()
		break