import socket
import threading


def send_message(name):
    while True:
        message = input()
        sock.send(bytes(name + ": " + message, "utf-8"))
        if message == "quit":
            sock.close()


def receive_message():
    while True:
        data = sock.recv(1024)
        if not data:
            break
        print(data.decode())


if __name__ == "__main__":
    sock = socket.socket()
    sock.connect(("localhost", 8000))
    name = input("Enter your name - ")
    threading.Thread(target=send_message, args=[name]).start()
    threading.Thread(target=receive_message).start()