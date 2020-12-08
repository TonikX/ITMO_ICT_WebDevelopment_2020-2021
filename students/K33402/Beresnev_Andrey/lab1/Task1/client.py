import socket

s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
s.connect((socket.gethostname(), 7777))

msg = s.recv(1024)
print(msg.decode("utf-8"))
s.send(bytes("Hello server", "utf-8"))
s.close()