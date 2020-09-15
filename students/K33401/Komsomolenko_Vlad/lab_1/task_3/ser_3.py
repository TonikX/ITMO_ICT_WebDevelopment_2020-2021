import socket
import time

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind( ("127.0.0.1", 14900) )
conn.listen(10)

while True:
	try:
		clientsocket, address = conn.accept()
		data = clientsocket.recv(16384)
		udata = data.decode("utf-8")
		print(udata)
		clientsocket.send(b"Hello, client.")
		html = open('index.html', 'r')
		text = html.read()
		clientsocket.send('HTTP/1.0 200 OK\nContent-Type: text/html\n\n{}'.format(text).encode())
		conn.close()
	except socket.error:
		print('waiting clients')
		time.sleep(1)
	except KeyboardInterrupt:
		conn.close()
		break

