"""Server sends a HEAD request to www.google.com""" 
import socket
import sys


HOST = socket.gethostname()
PORT = 1234
BUF_SIZE = 1024

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server.connect(('www.google.com' , 80))
except Exception as msg:
    print("Socket Error: %s" % msg)
    sys.exit()

request = b"HEAD / HTTP/1.1\r\nHost: www.google.com\r\nAccept: text/html\r\n\r\n"
server.sendall(request)  

print(server.recv(BUF_SIZE).decode("UTF-8"))

sys.exit()