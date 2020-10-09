import socket
import threading

sock = socket.socket()
sock.connect(('localhost', 9090))

def accepter():
	while True:
		data = sock.recv(1024)
		print(data.decode("utf-8"))

try:
	my_threard = threading.Thread(target=accepter)
	my_threard.start()
	while True:
		sock.send(input().encode("utf-8"))
except:
	print(e)
	sock.close()