import threading
import socket

name = "3"


def receive():
    try:
        while True:
            message = sock.recv(1024).decode()
            print(message)
    except ConnectionResetError:
        pass


def send():
    try:
        while True:
            message = (name + ": " + input()).encode()
            sock.send(message)
    except Exception:
        pass

if __name__ == '__main__':
    sock = socket.socket()
    sock.connect(('localhost', 9090))

    receive_thread = threading.Thread(target=receive)
    receive_thread.start()

    send_thread = threading.Thread(target=send)
    send_thread.start()

    receive_thread.join()
    send_thread.join()

    sock.close()
