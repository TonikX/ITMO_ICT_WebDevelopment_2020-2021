import socket
from threading import Thread
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 24003))

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

recieving = Thread(target=recieve)
sending = Thread(target=send)

recieving.start()
sending.start()