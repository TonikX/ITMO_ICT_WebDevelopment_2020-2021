import socket

sock = socket.socket()
sock.bind(('localhost', 9090))
sock.listen(1)

while True:
	try:
		conn, addr = sock.accept()
		data = conn.recv(1024)
		print(data.decode("utf-8"))
		conn.send('Hello, client!'.encode("utf-8"))
	except KeyboardInterrupt:
		conn.close()
		break