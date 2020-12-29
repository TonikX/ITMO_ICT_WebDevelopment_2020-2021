
import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()

while True:
    data = conn.recv(1024)
    if not data:
        break
    a, b, h = data.decode("utf-8").split()
    conn.send(str(( float(a) + float(b) )/ 2 * float(h)).encode("utf-8"))

conn.close()
