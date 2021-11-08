import socket
from threading import Thread
import threading


def get_user():
    while True:
        conn, addr = sock.accept()
        conns.append({"conn": conn, "socket": addr})
        print("connected:", addr)
        threading.Thread(target=receive, args=[conn]).start()

def receive(conn):
    while True:
        try:
            data = conn.recv(4096)
            message = str(data.decode("utf-8"))
            print(message)
            chat(conn, message)
        except:
            break

def chat(conn, message):
    for user in conns:
        if user["conn"] != conn:
            user["conn"].send(message.encode())


    
if __name__ == "__main__":
    sock = socket.socket()
    sock.bind(('', 9090))
    sock.listen(10)
    conns = []
    threading.Thread(target=get_user).start()
