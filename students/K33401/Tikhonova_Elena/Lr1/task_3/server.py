import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
    conn.bind(('localhost', 8080))
    conn.listen(10)

    clientsocket, address = conn.accept()

    data = clientsocket.recv(1024)
    print(data.decode())

    header = 'HTTP/1.1 200 OK\n'
    header += 'Content-Type: '+'text/html' + '\n\n'
    header = header.encode("utf-8")

    with open('index.html', 'rb') as index:
        response = index.read()
    clientsocket.sendall(header+response)
