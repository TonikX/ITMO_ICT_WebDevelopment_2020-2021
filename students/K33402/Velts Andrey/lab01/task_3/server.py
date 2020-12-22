import socket

sock = socket.socket()
sock.bind(("localhost", 9000))
sock.listen(1)

conn, addr = sock.accept()
conn.send(
    b"HTTP/1.0 200 OK\nContent-Type: text/html\n\n" + open("index.html", "rb").read()
)

conn.close()