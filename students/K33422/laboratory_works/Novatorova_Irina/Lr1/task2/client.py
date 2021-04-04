from socket import *
import sys

tcp_socket = socket(AF_INET, SOCK_STREAM)
tcp_socket.connect(("127.0.0.1", 14900))

data = input('send two legs: ')
if not data:
    tcp_socket.close()
    sys.exit(1)


tcp_socket.send(data.encode('utf-8'))
data = tcp_socket.recv(1024)
print(data.decode('utf-8'))

tcp_socket.close()