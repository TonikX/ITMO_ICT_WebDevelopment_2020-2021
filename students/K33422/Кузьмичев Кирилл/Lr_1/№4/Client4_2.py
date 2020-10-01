import socket
import threading

Sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Sock.connect(("127.0.0.2", 11042))

def send():
    while True:
        text = input()
        Sock.send(b"Polina: " + text.encode("utf-8"))

def get():
    while True:
        feedback = Sock.recv(1024)
        print(feedback.decode("utf-8"))

threading.Thread(target = send).start()
threading.Thread(target = get).start()