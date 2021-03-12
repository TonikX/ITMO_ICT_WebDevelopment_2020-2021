import socket
from threading import Thread

utf = "utf-8"
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 19400))

print("Welcome to the chat, enter 'Bye' to exit")


def send_message():
    while True:
        sock.send(input().encode(utf))


def receive_message():
    while True:
        data = sock.recv(16348)
        print(data.decode(utf))


send_thread = Thread(target=send_message)
get_thread = Thread(target=receive_message)

send_thread.start()
get_thread.start()