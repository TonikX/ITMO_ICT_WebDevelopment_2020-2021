import socket
import threading


server_adress = '127.0.0.1', 7777
s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
s.bind(('',0))

def readSocket():
    while 1:
        data = s.recv(1024)
        print(data.decode('utf-8'))

def runClient():
    print("Enter your name: ")
    nickname = input()
    s.sendto((nickname + ' Connect to server').encode('utf-8'),
                    server_adress)
    while 1:
        message = input()
        s.sendto((nickname + ': ' + message).encode('utf-8'), server_adress)

thread1, thread2 = threading.Thread(target=readSocket), threading.Thread(target=runClient)
thread1.start(), thread2.start()
