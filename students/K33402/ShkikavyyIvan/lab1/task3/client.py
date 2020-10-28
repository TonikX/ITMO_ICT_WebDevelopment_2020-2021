import socket

sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sckt.connect(('localhost', 8080))

while True:
    data = sckt.recv(1024)
    if not data:
        break
    print(data.decode("utf-8"))

sckt.close()
