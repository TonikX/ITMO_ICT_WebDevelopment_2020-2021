import socket

sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sckt.bind(('localhost', 8080))
sckt.listen(10)

while True:
    clientsocket, address = sckt.accept()
    print('connected:', address)
    data = clientsocket.recv(1024)
    if not data:
        break
    print(data.decode("utf-8"))
    clientsocket.sendall(b'Hello, client!')

clientsocket.close()
