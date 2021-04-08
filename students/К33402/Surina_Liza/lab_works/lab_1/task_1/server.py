import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(10)

conn, addr = sock.accept()
data = conn.recv(16384)
udata = data.decode("utf-8")
print("Client: " + udata)
conn.send(b"Hello, client.\n")

conn.close()
