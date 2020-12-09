import socket


conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(("127.0.0.1", 14915))
conn.listen(10)
clientsocket, addr = conn.accept()
while True:
    data = clientsocket.recv(1024)
    if not data:
        break
    with open('index.html', 'r') as file:
        html = file.read()
        clientsocket.sendall((f'HTTP/1.0 200 OK\nContent-Type: text/html\n\n{html}').encode())
conn.close()
