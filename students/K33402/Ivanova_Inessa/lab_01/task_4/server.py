import socket
import threading
import sys

sock = socket.socket()
sock.bind(("127.0.0.1", 14907))
sock.listen(10)
spisok = []

def recieve():
    while True:
        for connection in spisok:
            try:
                data = connection.recv(1024)
                if data:
                    print(connection, ':', data.decode())
            except socket.error as e:
                if e.errno == 10053:
                    print("Пользователй:", len(spisok))
                else:
                    raise

def send():
    while True:
        global spisok
        message = input()
        if message:
            for connection in spisok:
                connection.send(message.encode())

def accept():
    while True:
        global spisok
        spisok.append(sock.accept()[0])
        print("Пользователей:", len(spisok))

recieving = threading.Thread(target=recieve)
sending = threading.Thread(target=send)
accepting = threading.Thread(target=accept)
recieving.start()
sending.start()
accepting.start() 