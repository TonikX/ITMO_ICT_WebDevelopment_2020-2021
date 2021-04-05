import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("127.0.0.1", 9090))
conn.send(b"Give Http-message")

data = conn.recv(1024)
udata = data.decode("utf-8")
conn.close()

print(udata)