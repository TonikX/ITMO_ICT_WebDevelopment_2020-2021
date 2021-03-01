"""Server helps client find out length of the hypotenuse of a right triangle""" 
import socket
import math
import sys


HOST = socket.gethostname()
PORT = 1234
BUF_SIZE = 1024

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)
client_socket, address = server.accept()

msg = "Hello, client! We help you to find out length of the hypotenuse of a right triangle."
client_socket.send(bytes(msg, "UTF-8"))
a = int(client_socket.recv(BUF_SIZE).decode()) 
b = int(client_socket.recv(BUF_SIZE).decode())

result = str(math.sqrt(a*a + b*b))
response = "Length of the hypotenuse is: " + result

client_msg = client_socket.send(bytes(response, "UTF-8"))
if client_msg:
    print(client_socket.recv(BUF_SIZE).decode())
else:
    print("Server got trouble receiving client response!")

sys.exit()