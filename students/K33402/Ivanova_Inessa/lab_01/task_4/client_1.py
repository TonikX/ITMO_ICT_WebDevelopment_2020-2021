import socket
import threading
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1", 14907))

def recieve():
    while True:
        data = sock.recv(1024)
        if data:
            print(data.decode())

def send():
    while True:
        message = input()
        if message == "exit":
            sock.close()
            sys.exit()
        else:
            sock.send(message.encode())

recieving = threading.Thread(target=recieve)
sending = threading.Thread(target=send)

recieving.start()
sending.start() 