import socket

s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
s.bind((socket.gethostname(), 7777))
s.listen(1)

while True:
    client_socket, client_addr = s.accept()
    print(f"{client_addr} has connected")
    while True:
        data = client_socket.recv(1024)
        if not data:
            print(f"{client_addr} has disconnected")
            break
        with open('index.html', 'r') as file:
            html = file.read()
            client_socket.sendall(bytes(f'HTTP/1.0 200 OK\nContent-Type: text/html\n\n{html}', 'utf-8'))
    client_socket.close()
