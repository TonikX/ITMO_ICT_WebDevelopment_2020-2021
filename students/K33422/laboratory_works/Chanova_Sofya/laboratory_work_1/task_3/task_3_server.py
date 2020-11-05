import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 14006
server_socket.bind((host, port))
server_socket.listen(1)

print('starting server on: ', host, port, ' press ctrl+c to exit')

while True:
    try:
        client_socket, client_address = server_socket.accept()
        with open('index.html', 'r') as page:
            response_type = 'HTTP/1.0 200 OK\n'
            headers = 'Connect-Type: text/html\n\n'
            body = ''.join(page)
            response = response_type + headers + body
            client_socket.send(response.encode('utf-8'))
            client_socket.close()
    except KeyboardInterrupt:
        break

server_socket.close()
