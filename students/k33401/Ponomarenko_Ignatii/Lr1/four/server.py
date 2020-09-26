import socket
import threading

sock = socket.socket()
sock.bind(('localhost', 9090))
sock.listen(100)

connections = []

def conn_proccess(conn):
	while True:
		try:
			data = conn.recv(1024)
			for c in connections:
				if c != conn:
					try:
						c.send(data)
					except:
						if c in connections:
							connections.remove(c)
		except:
			if conn in connections:
				connections.remove(conn)

while True:
	conn, addr = sock.accept()
	connections.append(conn)
	my_threard = threading.Thread(target=conn_proccess, args=[conn])
	my_threard.start()