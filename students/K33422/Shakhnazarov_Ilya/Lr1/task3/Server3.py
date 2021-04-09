import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(("localhost", 23001))
conn.listen(1)

conn, addr = conn.accept()
conn.sendall(b"HTTP/1.0 200 OK\nContent-Type: text/html\n\n" + open("index.html", "rb").read())

conn.close()