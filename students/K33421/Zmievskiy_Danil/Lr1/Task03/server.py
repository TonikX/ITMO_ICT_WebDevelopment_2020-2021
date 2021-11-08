import socket

server = socket.socket()
host = '127.0.0.1'
port = 9090
server.bind((host, port))

print('Starting server on', host, port)
print('The Web server URL for this would be http://%s:%d/' % (host, port))

server.listen(5)

print('Entering infinite loop; hit Ctrl+C to exit')
while True:

	client, (client_host, client_port) = server.accept()
	print('Got conncetion from', client_host, client_port)
	while True:
		data = client.recv(1024)
		if not data:
			break
		response_type = 'HTTP/1.0 200 OK\n'
		headers = 'Content-Type: text/html\n\n'
		with open('index.html', 'r') as f:
			body = f.read()
		response = response_type + headers + body
		client.send(response.encode('utf-8'))
	client.close()