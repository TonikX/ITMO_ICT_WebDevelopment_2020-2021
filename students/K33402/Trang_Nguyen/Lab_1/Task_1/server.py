"""Server for the three first assignments."""

import socket
import math
import sys


HOST = socket.gethostname()
PORT = 1234
BUF_SIZE = 1024

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server.bind((HOST, PORT))
except Exception as msg:
    print("Socket Error: %s" % msg)
    sys.exit()

server.listen(5)
client_socket, address = server.accept()

while True:
    print(f"Got connection from {address}")

    client_msg = client_socket.recv(BUF_SIZE)
    print(client_msg.decode())

    client_socket.send(bytes("Hello, client!", "UTF-8"))
    sys.exit()