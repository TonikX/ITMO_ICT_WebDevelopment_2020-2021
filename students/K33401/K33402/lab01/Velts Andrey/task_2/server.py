import socket
import math

sock = socket.socket()
sock.bind(("localhost", 9000))
sock.listen(1)
conn, addr = sock.accept()

while True:
    data = conn.recv(1024)
    if not data:
        break
    print(data.decode("utf-8"))
    a, b = data.decode("utf-8").split()
    conn.send(str(math.sqrt(float(a) ** 2 + float(b) ** 2)).encode("utf-8"))

conn.close()