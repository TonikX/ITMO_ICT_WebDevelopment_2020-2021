import threading
import socket
import sys
import time


class Client:
    def __init__(self):
        super().__init__()
        self.kill = False
        self.host = "127.0.0.1"
        self.port = 3006

    def receive_history(self):
        data = str()
        while True:
            try:
                chunk = self.socket.recv(100)
                chunk = chunk.decode("UTF-8")
                data += chunk
                if "/end" in data:
                    break
            except socket.error:
                time.sleep(0.1)
                
        messages = data.split(';')
        if len(messages) > 1:
            for message in messages[:-1]:
                [client, text] = message.split('|')
                print(client + ": " + text)
        

    def connect(self):
        print("Connecting...")
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))
        self.socket.setblocking(False)

    def reading_socket(self):
        while not self.kill:
            try:
                data = self.socket.recv(1024)
                [client, text] = data.decode("UTF-8").split('|')
                print(client + ": " + text)
            except socket.error:
                time.sleep(0.3)

    def run(self):
        try:
            reading_thread = threading.Thread(target=self.reading_socket)
            reading_thread.start()
            nickname = input("Enter your nickname: ")
            self.socket.sendall(nickname.encode("UTF-8"))
            print("Connected successfuly")
            self.receive_history()

            while True:
                message = input()
                self.socket.sendall(message.encode("UTF-8"))
        except KeyboardInterrupt:
            self.kill = True
            print("Terminated")
            sys.exit(0)

client = Client()
client.connect()
client.run()



