import socket
import threading

class Client():
    def __init__(self):
        self.username = input('Enter your username: ')
        self.sock = socket.socket()
        self.sock.connect(('localhost', 5678))
        self.sock.sendall((self.username + ' endered chat').encode())
        print('You entered chat as ' + self.username)

    def send_messages(self):
        try:
            while True:
                msg = input()
                if msg == '\\quit':
                    print('You exited chat')
                    self.sock.sendall((self.username + ' exited chat').encode())
                    break
                self.sock.sendall((self.username + ': ' + msg).encode())
        except Exception:
            pass

    def check_messages(self):
        try:
            while True:
                new_msg = self.sock.recv(1024).decode()
                if new_msg:
                    print(new_msg)
        except Exception:
            pass

if __name__=='__main__':
    client = Client()
    threading.Thread(target=client.check_messages, args=()).start()
    threading.Thread(target=client.send_messages, args=()).start()
