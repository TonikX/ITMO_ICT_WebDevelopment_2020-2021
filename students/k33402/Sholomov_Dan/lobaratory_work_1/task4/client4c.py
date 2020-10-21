from threading import Thread
import socket


def send():
    data = input()
    while data != '/exit':
        sock.send(bytes(data, "utf-8"))
        data = input()
    sock.close()


def receive():
    while True:
        try:
            data = sock.recv(1024)
            print(data.decode('utf-8'))
        except OSError:
            exit()


if __name__ == "__main__":
    sock = socket.socket()
    sock.connect(('localhost', 44444))
    th_send, th_receive = Thread(target=send), Thread(target=receive)
    th_send.start(), th_receive.start()
