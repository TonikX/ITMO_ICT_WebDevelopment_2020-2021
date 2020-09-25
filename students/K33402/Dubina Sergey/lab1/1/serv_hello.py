import socket
import math

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 9090))
sock.listen()

n_sock, addr = sock.accept()
data = n_sock.recv(1024)

print(data.decode("utf-8"))
n_sock.send(bytes("Hello, client!!!!", "utf-8"))

n_sock.close()
