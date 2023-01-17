import socket

host = "127.0.0.1"
port = 9091
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(10)

while True:
	try:
		client_sock, client_addr = s.accept()

		data = client_sock.recv(16384)
		print("Получено (a, b, h): " + data.decode("utf-8"))

		a, b, h = data.split()
		area = (int(a) + int(b)) / 2 * int(h)
		response = str(area)
		client_sock.send(response.encode("utf-8"))

		print("Результат направлен к клиенту")

	except KeyboardInterrupt:
		s.close()
		break