import socket

sock = socket.socket()
sock.connect(('localhost', 9090))
S = input()
sock.send(S.encode("utf-8"))

data = sock.recv(1024)
sock.close()

print(data.decode("utf-8"))