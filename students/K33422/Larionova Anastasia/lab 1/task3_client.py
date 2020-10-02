import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 7775
sock.connect((host, port))

while True:
    data = sock.recv(1024)
    if not data:
        break
    print(data.decode('utf-8'))

sock.close()