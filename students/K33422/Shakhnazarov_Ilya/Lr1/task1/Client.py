import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("localhost", 21002))

conn.send(b"Hello, Server!")
conn.close()
