import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 14042
client_socket.connect((host, port))

while True:
    data = client_socket.recv(1024)
    if not data:
        break
    print(data.decode('utf-8'))

client_socket.close()

