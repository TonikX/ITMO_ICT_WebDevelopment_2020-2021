import socket

from threading import Thread
import time

users = []
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 53330))
sock.listen(10)
sock.setblocking(False)


def coming_users():
    while True:
        sock.setblocking(True)
        clientsoc, addr = sock.accept()
        sock.setblocking(False)
        if clientsoc not in users:
            users.append((clientsoc, addr))
            print('User connected:', addr)


def message():
    while True:
        text = None
        try:
            for user in users:
                text = user[0].recv(1024).decode('utf-8')
                print('Received text: ' + text)
                if text == "close":
                    user[0].close()
                    print('User have closed chat: ', user[1])
                    text = f'User {user[1]} have closed chat'
                for send_user in users:
                    if send_user[0] == user[0]:
                        continue
                    data = f'User {user[1]}: ' + text
                    send_user[0].sendall(data.encode('utf8'))
        except socket.error:
            print('waiting...')
            time.sleep(1)
        except KeyboardInterrupt:
            for user in users:
                user[0].close()
            break


user_thread = Thread(target=coming_users)
message_thread = Thread(target=message)

user_thread.start()
message_thread.start()