import socket
import threading
import random


def send_message():
    try:
        while True:
            msg = input()
            sock.send(bytes(name + ": " + msg, 'utf-8'))
            if msg == '\leave chat':
                sock.close()
                break
    except Exception:
        pass
    finally:
        print('You left chat.')


def receive_message():
    try:
        while True:
            data = sock.recv(1024).decode('utf-8')
            if not data:
                break
            print(data)
        sock.close()
    except Exception:
        pass



sock = socket.socket()
sock.connect(('localhost', 9090))
number = random.randint(0,1000)
name = "person" + str(number)
threading.Thread(target=send_message).start()
threading.Thread(target=receive_message).start()
