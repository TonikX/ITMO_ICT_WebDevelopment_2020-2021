import socket

s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
s.connect((socket.gethostname(), 9090))

s.sendall(bytes(f'.', 'utf-8'))
data = s.recv(1024)
print(data.decode('utf-8'))
s.close()