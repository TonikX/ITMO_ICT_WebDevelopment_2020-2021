from socket import *
from threading import Thread
import sys


HOST = gethostname()
PORT = 1234
BUF_SIZE = 1024
CLIENT_SOCKET = socket(AF_INET, SOCK_STREAM)
CLIENT_SOCKET.connect((HOST, PORT))


def receive():
    while True:
        msg = CLIENT_SOCKET.recv(BUF_SIZE).decode("UTF-8")

        if not msg:
            break
        print(msg)


def send():
    while True:
        msg = input()
        if msg:
            CLIENT_SOCKET.send(bytes(msg, "UTF-8"))
        if msg == "q":
            sys.exit()


if __name__ == "__main__":
    while True:
        receive_thread = Thread(target=receive)
        send_thread = Thread(target=send)
        receive_thread.start()
        send_thread.start()
        send_thread.join()
        receive_thread.join()
    
    sys.exit()