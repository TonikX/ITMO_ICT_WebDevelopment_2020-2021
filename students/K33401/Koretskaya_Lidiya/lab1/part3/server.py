import socket

host = "127.0.0.1"
port = 9091
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(10)


while True:
	try:
		client_sock, client_addr = s.accept()

		file = open('index.html', 'r')
		data = file.read()
		client_sock.send('HTTP/1.0 200 OK\nContent-Type: text/html\n\n{}'.format(data).encode())


	except KeyboardInterrupt:
		s.close()
		break

