import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 14006
client_socket.connect((host, port))

data = client_socket.recv(1024)

print(data.decode('utf-8'))

client_socket.close()
