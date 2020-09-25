import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 9090))

a = sock.recv(1024)
print(a.decode("utf-8"))
num = input()
sock.send(bytes(num, "utf-8"))

b = sock.recv(1024)
print(b.decode("utf-8"))
num = input()
sock.send(bytes(num, "utf-8"))

c = sock.recv(1024)
print(c.decode("utf-8"))
num = input()
sock.send(bytes(num, "utf-8"))

msg = sock.recv(1024)
print(msg.decode("utf-8"))

sock.close()
