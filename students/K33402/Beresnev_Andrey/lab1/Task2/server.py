import socket
from math import sqrt

s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
s.bind((socket.gethostname(), 7777))
s.listen(1)

while True:
    client_socket, client_addr = s.accept()
    print(f"Connected client from {client_addr}")

    client_socket.send(bytes("In order to calculate bisector I need to know legs", "utf-8"))
    leg1, leg2 = client_socket.recv(1024).decode("utf-8").split(',')
    leg1 = int(leg1)
    leg2 = int(leg2)
    bisector = sqrt(leg1 ** 2 + leg2 ** 2)
    client_socket.send(bytes(f"Hypotenuse: {bisector}", "utf-8"))
    client_socket.close()
