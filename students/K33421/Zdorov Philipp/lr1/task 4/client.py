import socket
from threading import Thread
import json


class Client:
    def __init__(self, name):
        self.name = name
        self.sock = socket.socket()
        self.sock.connect(('localhost', 9090))
        self.is_online = True

    def receive(self):
        while self.is_online:
            try:
                data = json.loads(self.sock.recv(1024).decode())
                print(f'{data.get("name")}: {data["message"]}')
            except ConnectionAbortedError:
                exit()

    def send(self):
        while self.is_online:
            message = input()
            self.sock.send(json.dumps({'message': message, 'name': self.name}).encode())
            if message == '/quit':
                self.sock.close()
                self.is_online = False


if __name__ == '__main__':
    name = input('name: ')
    client = Client(name)
    Thread(target=client.send).start()
    Thread(target=client.receive).start()
