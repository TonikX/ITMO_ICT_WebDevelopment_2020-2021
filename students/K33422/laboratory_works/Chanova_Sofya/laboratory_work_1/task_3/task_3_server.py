import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 14042
server_socket.bind((host, port))


print('starting server on: ', host, port, ' press ctrl+c to exit')

server_socket.listen(1)
client_socket, client_address = server_socket.accept()

while True:
    with open('index.html', 'r') as page:
        response_type = 'HTTP/1.0 200 OK\n'
        headers = 'Connect-Type: text/html\n\n'
        body = ''.join(page)
        response = response_type + headers + body
        client_socket.send(response.encode('utf-8'))
    data = client_socket.recv(1024)
    if not data:
        break

client_socket.close()

