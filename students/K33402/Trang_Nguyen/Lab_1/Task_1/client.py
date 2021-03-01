import socket

HOST = socket.gethostname()
PORT = 1234
BUF_SIZE = 1024

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

client.send(bytes("Hello, server!", "UTF-8"))
server_msg = client.recv(BUF_SIZE)
print(server_msg.decode("UTF-8"))

client.close()