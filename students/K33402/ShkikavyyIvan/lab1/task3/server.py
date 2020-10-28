import socket

sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sckt.bind(('localhost', 8080))
sckt.listen(1)
while True:
    clientsocket, address = sckt.accept()
    with open('index.html', 'r') as file:
        html = file.read()
        clientsocket.sendall(bytes(f'HTTP/1.0 200 OK\nContent-Type: text/html\n\n{html}', 'utf-8'))
    data = clientsocket.recv(1024)
    if not data:
        break

clientsocket.close()
