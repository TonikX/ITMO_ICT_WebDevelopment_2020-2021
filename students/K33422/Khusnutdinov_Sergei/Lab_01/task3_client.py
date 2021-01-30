import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 9090))

while True:
	data = client.recv(1024)
	if not data:
		break
	print(data.decode('utf-8'))

client.close()