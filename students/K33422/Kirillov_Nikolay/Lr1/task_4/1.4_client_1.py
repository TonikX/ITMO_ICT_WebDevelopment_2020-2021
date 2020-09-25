import socket
import threading


def read_sok():
    while True:
        data = sor.recv(1024)
        print(data.decode('utf-8'))


server = 'localhost', 9090
name = input('Enter your nickname: ')
sor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sor.bind(('', 0))
sor.sendto((name + ' Connect to server').encode('utf-8'), server)
stream = threading.Thread(target=read_sok)
stream.start()
while True:
    message = input()
    sor.sendto(('[' + name + '] ' + message).encode('utf-8'), server)
