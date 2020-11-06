import socket
import os
import codecs

server = socket.socket()
host = "127.0.0.1"
port = 536
server.bind((host, port))

server.listen(5)
count = 0
while True:
    client, (client_host, client_port) = server.accept()
    req = client.recv(1024)
    req = req.decode("UTF-8")
    responce_type = "HTTP/1.0 200 OK\n"
    headers = 'Content-Type: text/html\n'
    responce_type = responce_type.encode()
    client.send(responce_type)
    headers = headers.encode()
    client.send(headers)
    index_file = open(os.path.join(os.path.dirname(__file__), 'index.html'), "r")
    http_response = index_file.read()
    body =  '''
     '''
    body += http_response
    print(body)
    client.sendall(body.encode("utf-8"))
    client.close()
