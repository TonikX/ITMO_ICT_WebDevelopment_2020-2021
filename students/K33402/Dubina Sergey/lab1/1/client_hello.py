import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 9090))

sock.send(bytes("Hello, server!!!", "utf-8"))

data = sock.recv(1024)

print(data.decode("utf-8"))




