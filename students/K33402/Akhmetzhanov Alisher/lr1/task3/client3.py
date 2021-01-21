import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 9090))

while True:
    data = sock.recv(1024)
    if not data:
        break
    print(data.decode("utf-8"))

sock.close()