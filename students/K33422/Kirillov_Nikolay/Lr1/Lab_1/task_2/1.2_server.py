import socket
from math import sqrt

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()

data = conn.recv(1024)
leg1 = data.decode('utf-8').split()[0]
leg2 = data.decode('utf-8').split()[1]
hyp = sqrt(float(leg1)**2 + float(leg2)**2)
conn.sendall(str(hyp).encode('utf-8'))

conn.close()
