import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 8880
server.bind((host, port))

print("Starting server on", host, port)
print("The web server URL for this would be http://%s:%d/" % (host, port))

server.listen(1)

print("Entering...")

while True:
	client, (client_host, client_port) = server.accept()
	print("Got connection from", client_host, client_port)

	response_type = "HTTP/1.1 200 OK\n"
	headers = "Content-Type: text/html\n\n"

	body = open("index.html", "r").read()
	response = response_type + headers + body

	client.sendall(response.encode())

	data = client.recv(1024)
	if not data:
		break

client.close()