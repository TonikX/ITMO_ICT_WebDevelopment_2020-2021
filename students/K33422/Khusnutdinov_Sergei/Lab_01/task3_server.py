import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 9090))
server.listen(1)
print("Server is on...")

conn, addr = server.accept()
print('Connected: ', addr)

while True:
	with open('index.html', 'r') as page:
		response_type = 'HTTP/1.0 200 OK \n'
		headers = 'Content-Type: text/html \n\n'
		body = ''.join(page)
		response = response_type + headers + body
		conn.send(response.encode('utf-8'))
	data = conn.recv(1024)
	if not data:
		break
	conn.close()

server.close()