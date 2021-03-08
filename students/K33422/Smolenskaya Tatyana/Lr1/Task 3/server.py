import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 8888))
sock.listen(1)
conn, addr = sock.accept()

print('connected: ', addr)

while True:
    data = conn.recv(1024)
    if not data:
        break
    with open('index.html', 'r') as file:
        html = file.read()
        conn.sendall((f'HTTP/1.0 200 OK\nContent-Type: text/html\n\n{html}').encode())

conn.close()
