import socket
from threading import Thread
import threading


class Server:

    def __init__(self):
        s.bind(('localhost', 9090))
        s.listen(10)
        print("Server started on socket:", s)
        print("Waiting for users...")

    def get(self):
        while True:
            client, ad = s.accept()
            clients.append({"connection": client, "socket": ad})
            print("connected:", ad)
            Thread(target=self.check, args=(client,)).start()

    def check(self, client):
        while True:
            try:
                data = client.recv(4096)
                message = str(data.decode("utf-8"))
                self.bcast(client, message)
            except Exception as ex:
                self.delete(client)
                break

    def delete(self, client):
        for user in clients:
            if user["connection"] == client:
                clients.remove(user)
                break

    def bcast(self, client, message: str):
        message += "\n"
        for user in clients:
            if user["connection"] != client:
                user["connection"].send(message.encode())


if __name__ == "__main__":
    s = socket.socket()
    clients = []
    server = Server()
    thread = threading.Thread(target=server.get())
    thread.start()
    thread.join()
