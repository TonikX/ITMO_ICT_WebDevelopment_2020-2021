import socket
import threading


# получаем сообщения от сервера
def read_sok():
    while True:
        sock = sor.recv(1024)
        print(sock.decode('utf-8'))


server = 'localhost', 9090
print("What's your name?")
name = input()  # вводим имя пользователя
sor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sor.bind(('', 0))
# Уведомляем сервер о подключении
sor.sendto((name+' connected to server').encode('utf-8'), server)
print("You're in. Lets chat!")
thread = threading.Thread(target=read_sok)
thread.start()
while True:
    message = input()
    sor.sendto(('['+name+']'+message).encode('utf-8'), server)
