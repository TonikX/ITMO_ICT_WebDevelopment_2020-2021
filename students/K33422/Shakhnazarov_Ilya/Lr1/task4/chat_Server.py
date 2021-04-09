import socket
from threading import Thread
import sys

sock = socket.socket()
sock.bind(("localhost", 24003))
sock.listen(10)
arr = []

def recieve():
    while True:
        for connection in arr:
            try:
                data = connection.recv(1024)
                if data:
                    print(connection, ':', data.decode())
            except socket.error as e:
                if e.errno == 10053:
                    print("Users amount - ", len(arr))
                else:
                    raise

def send():
    while True:
        global arr
        message = input()
        if message:
            for connection in arr:
                connection.send(message.encode())

def accept():
    while True:
        global arr
        arr.append(sock.accept()[0])
        print("Users amount - ", len(arr))

recieving = Thread(target=recieve)
sending = Thread(target=send)
accepting = Thread(target=accept)

recieving.start()
sending.start()
accepting.start()