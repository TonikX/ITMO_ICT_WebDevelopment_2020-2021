import socket

sock = socket.socket()
sock.connect(("localhost", 9000))

while True:
    data = sock.recv(1024)
    if not data:
        break
    print(data.decode("utf-8"))


sock.close()