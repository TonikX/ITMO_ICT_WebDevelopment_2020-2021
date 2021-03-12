import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect (("127.0.0.1", 14900))
hels = "Hello, server"
conn.send(bytes(hels, "utf-8"))

data = conn.recv(16384)
udata = data.decode("utf-8")
print(udata)

conn.close()