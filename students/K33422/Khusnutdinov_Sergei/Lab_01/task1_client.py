import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 9090))
client.send('Hello, server'.encode('utf-8'))

data = client.recv(1024)
print(data.decode('utf-8'))

client.close()