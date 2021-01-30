import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', 9090))
server.listen(1)
conn, addr = server.accept()

print('Connected: ', addr)

while True:
	data = conn.recv(1024)
	if not data:
		break
	print(data.decode('utf-8'))
	conn.send('Hello, client'.encode('utf-8'))

server.close()