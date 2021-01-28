import socket

sock = socket.socket()
sock.bind(('localhost', 9000))
sock.listen(1)
conn, addr = sock.accept()

while True:
    data = conn.recv(1024)
    if not data:
         break
    print(data.decode("utf-8"))
    conn.send(b'Hello, client!')

conn.close()