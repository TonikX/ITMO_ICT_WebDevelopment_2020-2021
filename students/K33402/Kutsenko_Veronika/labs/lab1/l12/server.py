import socket
from math import sqrt

s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
s.bind((socket.gethostname(), 9090))
s.listen(1)

while True:
    client_socket, client_addr = s.accept()
    print(f"Connected client from {client_addr}")

    client_socket.send(bytes("Введите стороны треугольника:", "utf-8"))
    leg1, leg2 = client_socket.recv(1024).decode("utf-8").split(',')
    leg1 = int(leg1)
    leg2 = int(leg2)
    res = sqrt(leg1 ** 2 + leg2 ** 2)
    client_socket.send(bytes(f"Гиппотенуза: {res}", "utf-8"))
    client_socket.close()