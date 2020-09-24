import socket
import threading

sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sckt.connect(('localhost', 9090))
name = input('Введите ник: ')


def send_message():
    try:
        while True:
            text = input()
            sckt.sendall(bytes(name + ": " + text, "utf-8"))
            if text == "X":
                sckt.close()
                break
    except Exception:
        pass


def get_message():
    try:
        while True:
            data = sckt.recv(1024).decode("utf-8")
            if not data:
                break
            print(data)
        sckt.close()
    except Exception:
        pass


threading.Thread(target=send_message).start()
threading.Thread(target=get_message).start()
