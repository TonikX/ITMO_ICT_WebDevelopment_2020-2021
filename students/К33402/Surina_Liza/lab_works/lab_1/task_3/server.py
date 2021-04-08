import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("localhost", 9090))
sock.listen(10)

conn, add = sock.accept()
file = open("index.html", "r")
text = file.read()
conn.send('HTTP/1.0 200 OK\nContent-Type: text/html\n\n{}'.format(text).encode())
sock.close()
