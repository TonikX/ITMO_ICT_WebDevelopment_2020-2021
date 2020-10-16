import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.connect(('localhost', 8080))
    s.send(b"GET / HTTP/1.1\r\nHost: localhost:8080\r\nAccept: text/html\r\n\r\n")

    while True:
        data = s.recv(1024)
        if not data:
            break
        print(data.decode())
