import socket
import time

server = socket.socket()
host = 'localhost'
port = 555
server.bind((host,port))

print ('Starting server on', host, port)

server.listen(5)

quit = False

while not quit:
	try:
		client, (client_host, client_port) = server.accept()
		print('New connection', client_host, client_port)
		responce_type = 'HTTP/1.0 200 OK\n'
		headers = 'Content-Type: text/html\n\n'
		content = open('index.html', 'r')
		body = ''. join(content)
		responce = responce_type + headers + body
		client.send(responce.encode('utf-8'))
		client.close()
	except KeyboardInterrupt:
		quit = True
		print("Server stopped")
server.close()