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
    text = open("index.html").read()
    text = bytes(f'HTTP/1.0 200 OK\nContent-Type: text/html\n\n{text}', 'utf-8')
    conn.send(text)

conn.close()