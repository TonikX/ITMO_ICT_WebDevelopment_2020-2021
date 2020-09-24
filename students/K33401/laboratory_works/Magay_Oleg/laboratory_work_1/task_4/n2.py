import socket
import threading

enc = "UTF-8"
user = "n2"


def get():
    try:
        while True:
            message = s.recv(1024).decode(enc)
            print(message)
    except ConnectionResetError:
        pass


def send():
    try:
        while True:
            message = (user + ": " + input()).encode(enc)
            s.send(message)
    except Exception:
        pass


if __name__ == '__main__':
    s = socket.socket()
    s.connect(('localhost', 9090))

    get_message_thread = threading.Thread(target=get)
    get_message_thread.start()

    send_message_thread = threading.Thread(target=send)
    send_message_thread.start()

    get_message_thread.join()
    send_message_thread.join()

    s.close()
