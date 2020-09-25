import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()
print('connected:', addr)

while True:

    data = conn.recv(1024)
    print(data.decode("utf-8"))
    if not data:
        break
    conn.send(bytes("Hello, client!", "utf-8"))

conn.close()
