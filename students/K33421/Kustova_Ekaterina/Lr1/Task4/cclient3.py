import socket
import threading

# Задание №4
# КЛИЕНТ
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("127.0.0.1", 14900))


def outgoing():
    while True:
        message = input()
        conn.send(b"Client 3: " + message.encode("utf-8"))


def incoming():
    while True:
        a = conn.recv(1024)
        print(a.decode("utf-8"))


threading.Thread(target=outgoing).start()
threading.Thread(target=incoming).start()
