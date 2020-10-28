from threading import Thread
import socket


def connect():
    while True:
        conn, addr = sock.accept()
        users.append([conn,  addr])
        print(addr)
        th_listen = Thread(target=resend, args=(conn,))
        th_listen.start()


def resend(conn):
    while True:
        try:
            data = conn.recv(1024)
            message = str(data.decode("utf-8"))
            for user in users:
                if user[0] != conn:
                    user[0].send(message.encode())
        except Exception:
            for user in users:
                if user["connection"] == conn:
                    users.remove(user)
            break


if __name__ == "__main__":
    sock = socket.socket()
    sock.bind(('localhost', 44444))
    sock.listen(10)
    users = []
    connect()
