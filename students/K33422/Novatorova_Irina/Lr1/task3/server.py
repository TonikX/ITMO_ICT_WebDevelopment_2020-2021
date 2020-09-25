import socket
import codecs

server = socket.socket()
host = '127.0.0.1'
port = 14900
server.bind((host, port))
server.listen(5)

print('Entering infinite loop; hit Ctrl+C to exit')
while True:
    client, (client_host, client_port) = server.accept()
    print('Got connection from', client_host, client_port)
    response_type = 'HTTP/1.0 200 Ok\n'
    headers = 'Content-Type: text/html\n\n'
    page = codecs.open("index.html")
    body = ''.join(page)
    response = response_type + headers + body
    client.sendall(response.encode('utf-8'))
    client.close()