import socket

s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
s.bind((socket.gethostname(), 7777))
s.listen(1)

while True:
    client_socket, client_addr = s.accept()
    print(f"Connected client from {client_addr}")

    client_socket.send(bytes("Hello client", "utf-8"))
    print(client_socket.recv(1024).decode("utf-8"))
    client_socket.close()
