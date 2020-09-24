import socket
import threading

sock = socket.socket()
sock.bind(('localhost', 9090))
sock.listen(200)

def conn_proccess(conn):
	data = conn.recv(1024)
	for c in connections:
		if c != conn:
			c.send(data)	

	# print(data.decode("utf-8"))
	# conn.send('Hello, client!'.encode("utf-8"))

while True:
	try:
		conn, addr = sock.accept()
		connections.append(conn)
		threading.Thread(target=conn_proccess, args=[conn])
	except KeyboardInterrupt:
		conn.close()
		break