import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 8080))
sock.listen(1)
clientsoc, addr = sock.accept()
print('connected:', addr)

while True:
    data = clientsoc.recv(1024)
    if not data:
        break
    print(data.decode("utf-8"))
    clientsoc.sendall(b'Hello, client!')

clientsoc.close()