import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(10)
conn, addr = sock.accept()

while True:
    data = conn.recv(1024)
    data = str(data.decode())
    print(data)
    if not data:
        break
    conn.send('Hello, client'.encode())

conn.close()