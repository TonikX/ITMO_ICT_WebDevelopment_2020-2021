import socket

sock = socket.socket()
sock.bind(('localhost', 9090))
sock.listen(1)

while True:
	try:
		conn, addr = sock.accept()
		data = conn.recv(1024*8)
		body = open('index.html').read()
		print(body)
		S = 'HTTP/1.1 200 OK\n'
		S += 'Content-Type: text/html; charset=utf-8\n'
		S += 'Content-Length: ' + str(len(body)) + '\n\n'
		S += body
		conn.send(S.encode("utf-8"))
	except KeyboardInterrupt:
		conn.close()
		break