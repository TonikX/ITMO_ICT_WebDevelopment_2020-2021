import socket

server = socket.socket()
host = "127.0.0.1"
port = 8000
server.bind((host, port))

print("Starting server on", host, port)
print("The web server URL for this would be http://%s:%d/" % (host, port))

server.listen(5)

print("Entering...")
while True:
	client, (client_host, client_port) = server.accept()
	print("Got connection from", client_host, client_port)

	response_type = "HTTP/1.0 200 OK\n"
	headers = "Content-Type: text/html\n\n"
	body = open("index.html", "r").read()

	response = response_type + headers + body
	client.send(response.encode())
	client.close()