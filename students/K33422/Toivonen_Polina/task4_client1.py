import socket
from threading import Thread


def send_message():
    while True:
        s.send(input().encode('utf-8'))


def receive_message():
    while True:
        data = s.recv(1024)
        print(data.decode('utf-8'))


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 8888))

send_th = Thread(target=send_message)
get_th = Thread(target=receive_message)

send_th.start()
get_th.start()