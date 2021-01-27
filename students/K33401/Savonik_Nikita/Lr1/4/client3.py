import socket
from threading import Thread


def send_message():
    while True:
        text = input()
        sock.sendall(bytes(text, "utf-8"))
        if text == "exit":
            sock.close()
            break


def receive_message():
    while True:
        data = sock.recv(1024)
        print(data.decode("utf-8"))



sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 53330))
send_thread = Thread(target=send_message)
get_thread = Thread(target=receive_message)

send_thread.start()
get_thread.start()