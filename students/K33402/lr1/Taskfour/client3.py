import socket
import threading


class Client:
    def __init__(self):
        self.server = '127.0.0.1', 14900  # Данные сервера
        self.sor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sor.bind(('', 0))  # Задаем сокет как клиент


    def read_sok(self):
        while 1:
            data = self.sor.recv(1024)
            print(data.decode('utf-8'))

    def runClient(self):
        print("Enter your name: ")
        self.alias = input()  # Вводим наш псевдоним
        self.sor.sendto((self.alias + ' Connect to server').encode('utf-8'),
                        self.server)  # Уведомляем сервер о подключении
        while 1:
            mensage = input()
            self.sor.sendto((self.alias + ': ' + mensage).encode('utf-8'), self.server)


if __name__ == '__main__':
    Client = Client()
    potok1, potok2 = threading.Thread(target=Client.read_sok), threading.Thread(target=Client.runClient)
    potok1.start(), potok2.start()
