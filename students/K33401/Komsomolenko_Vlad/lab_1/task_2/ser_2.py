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
		clientsocket.send(b"Hello, client. h, a, b = ?\n")
		data = clientsocket.recv(16384)
		udata = data.decode("utf-8")
		info = udata.split(', ')
		h = int(info[0])
		a = int(info[1])
		b = int(info[2])
		s = 0.5*h*(a+b)
		s = str(s)
		clientsocket.send(s.encode())
		conn.close()
	except socket.error:
		print('waiting clients')
		time.sleep(1)
	except KeyboardInterrupt:
		conn.close()
		break
