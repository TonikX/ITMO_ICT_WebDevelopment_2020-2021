import socket
import math

print("Waiting for connections...")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 9090))
sock.listen()

n_sock, addr = sock.accept()

print("Client connected! Trying to solve equation")
data = n_sock.recv(1024)

t = data.decode("utf-8")

a = int(t[0])
b = int(t[1])
c = int(t[2])

d = b*b - 4 * a * c

if d > 0:
	x1 = (-(int(t[1])) + math.sqrt(d))/(2 * int(t[0]))
	x2 = (-(int(t[1])) - math.sqrt(d))/(2 * int(t[0]))
	x = f"x1: {x1} x2: {x2}"
elif d == 0:
	x_ = str(-(int(t[1]))/(2 * int(t[0])))
	x = f"x: {x_}"
elif d < 0:
	x = 'biba'


n_sock.send(bytes(str(x), "utf-8"))

n_sock.close()
