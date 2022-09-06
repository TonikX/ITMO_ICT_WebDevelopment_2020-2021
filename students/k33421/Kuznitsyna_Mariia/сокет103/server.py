import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established")

    clientsocket.sendall(b'HTTP/1.0 200 OK\nContent-Type: text/html\n' + open('file.html', 'r').read())

clientsocket.close()