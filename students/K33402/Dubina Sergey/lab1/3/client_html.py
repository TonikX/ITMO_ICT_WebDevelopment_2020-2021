import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 9090))


data = sock.recv(1024)

sock.close()

print(data.decode("UTF-8"))


