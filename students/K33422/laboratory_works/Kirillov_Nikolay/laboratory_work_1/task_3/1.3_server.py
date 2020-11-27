import socket
import codecs

server = socket.socket()
host = '127.0.0.1'
port = 555
server.bind((host, port))

link = str('http://%s:%d' % (host, port))

server.listen(5)

print('Entering infinite loop; hit Ctrl+C to exit')
while True:
    client, (client_host, client_port) = server.accept()
    client.sendall(link.encode('utf-8'))
    print('Got connection from', client_host, client_port)
    client.recv(1000)
    response_type = 'HTTP/1.0 200 Ok\n'
    headers = 'Content-Type: text/html\n\n'
    body = codecs.open("index.html")
    response = response_type + headers + body.read()
    client.sendall(response.encode('utf-8'))
    client.close()
