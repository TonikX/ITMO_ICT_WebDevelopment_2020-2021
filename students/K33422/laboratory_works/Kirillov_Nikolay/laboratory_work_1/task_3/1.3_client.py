import socket

client = socket.socket()
client.connect(('127.0.0.1', 555))

data = client.recv(1024)
client.close()

print(data.decode('utf-8'))
