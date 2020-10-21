import socket
import threading
import sys

sock = socket.socket()
sock.bind(('localhost', 9090))
sock.listen(10)
conn = []

def Reciver():
    while 1:
        for i in range(len(conn)):
            try:
                data = conn[i].recv(1024)
                if data:
                    print(data.decode())
            except socket.error as e:
                if e.errno == 10053:
                    conn.pop(i)
                    print("Подключено пользователй:", len(conn))
                else:
                    raise

def Sender():
    while 1:
        global conn
        message = input()
        if message:
            for i in range(len(conn)):
                conn[i].send(message.encode())

def Accepter():
    while 1:
        global conn
        conn.append(sock.accept()[0])
        print("Подключено пользователй:", len(conn))


# init threads
t1 = threading.Thread(target=Reciver)
t2 = threading.Thread(target=Sender)
t3 = threading.Thread(target=Accepter)

# start threads
t1.start()
t2.start()
t3.start()