import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 8080))
sock.listen(1)
clientsoc, addr = sock.accept()
print('connected:', addr)

while True:
    with open('index.html', 'r') as file:
        html = file.read()
        clientsoc.sendall(bytes(f'HTTP/1.0 200 OK\nContent-Type: text/html\n\n{html}', 'utf-8'))
    data = clientsoc.recv(1024)
    if not data:
        break


clientsoc.close()
