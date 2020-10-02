import socket
from threading import Thread

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 12345))

nick = input('Who are you?\n')
print("Welcome to the chat, enter 'q' to quit")


def send_message():
    while True:
        message = (f'{nick}: {input("")}')
        sock.send(message.encode('utf-8'))


def receive_message():
    while True:
        data = sock.recv(4096)
        print(data.decode('utf-8'))


send_thread = Thread(target=send_message)
get_thread = Thread(target=receive_message)
send_thread.start()
get_thread.start()