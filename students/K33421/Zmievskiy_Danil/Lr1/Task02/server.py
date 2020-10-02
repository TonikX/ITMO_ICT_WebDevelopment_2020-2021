import socket

def parall_area(data):
	a, h = map(int, data.split())
	S = a * h
	return str(S)

if __name__ == '__main__':

	conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	conn.bind(("127.0.0.1", 9090))
	conn.listen(10)

	while True:
		try:
			clientsocket, address = conn.accept()
			data = clientsocket.recv(1024)
			data.decode('utf-8')
			result = parall_area(data)
			clientsocket.send(result.encode('utf-8'))
			clientsocket.close()
		except KeyboardInterrupt:
			conn.close()
			break
