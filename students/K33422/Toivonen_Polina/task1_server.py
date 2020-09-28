import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 7777))
s.listen(1)
conn, addr = s.accept()

while True:
    data = conn.recv(1024)
    if not data:
        break
    print(data.decode("utf-8"))
    conn.send(b"Hello, client!")
conn.close()
