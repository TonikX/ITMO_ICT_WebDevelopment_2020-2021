import socket
from threading import Thread
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 8888))
s.listen(10)
s.setblocking(False)
users = []


def new_users():
    while True:
        s.setblocking(True)
        clientsocket, addr = s.accept()
        s.setblocking(False)
        if clientsocket not in users:
            users.append((clientsocket, addr))
            print('New user:', addr)


def chat():
    while True:
        try:
            for user in users:
                message = user[0].recv(1024).decode('utf-8')
                print(user[-1], '`s message: ' + message)
            for send_user in users:
                    if send_user[0] == users[0]:
                        continue
                    data = f'User {users[1]}: ' + message
                    send_user[0].send(data.encode('utf8'))
        except socket.error:
            time.sleep(5)
        except KeyboardInterrupt:
            for user in users:
                users[0].close()
            break


user_th = Thread(target=new_users)
chat_th = Thread(target=chat)

user_th.start()
chat_th.start()