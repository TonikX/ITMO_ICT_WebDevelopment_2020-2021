import socket
from threading import Thread
import threading
import math

class Server:

    def __init__(self):
        s.bind(('localhost', 9090))
        s.listen(10)
        print("Server started on socket:", s)
        print("Wait for users...")

    def get(self):
        while True:
            client, ad = s.accept()
            clients.append({"connection": client, "socket": ad})
            print("connected:", ad)
            Thread(target=self.check, args=(client,)).start()
    def area(self):
        while True:
	        try:
                s, ad = s.accept()
                data = s.recv(16384)
                u = data.decode("utf-8")
                print(u)
                s.send("Hello, client. a, b, c = ?")
                data = s.recv(16384)
                u = data.decode("utf-8")
                info = u.split(', ')
                a = int(info[0])
                b = int(info[1])
                c = int(info[2])
                area = 0.5*h*(a+b)
                area = str(s)
                clientsocket.send(s.encode())
                conn.close()


    def delete(self, client):
        print("delete", client)
        for user in clients:
            if user["connection"] == client:
                clients.remove(user)
                break


    def target(self, client, message):
        message += "\n"
        client.send(message.encode())

if __name__ == "__main__":
    s = socket.socket()
    clients = []
    server = Server()
    thread = threading.Thread(target=server.get())
    thread.start()
    thread.join()
