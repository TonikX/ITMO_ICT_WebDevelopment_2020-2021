import socket
from threading import Thread
import threading


class Server:
    def __init__(self):
        sock.bind(("localhost", 8000))
        sock.listen(10)
        self.connections = []

    def get_socket(self):
        while True:
            connection, addr = sock.accept()
            self.connections.append({"user": connection, "socket": addr})
            print("connected:", addr)
            Thread(target=self.check_messages, args=(connection,)).start()

    def check_messages(self, connection):
        while True:
            try:
                data = connection.recv(4096)
                message = str(data.decode())
                self.send_message(connection, message)
            except Exception as ex:
                self.remove_user(connection)
                break

    def remove_user(self, user):
        for connection in self.connections:
            if connection["user"] == user:
                self.connections.remove(connection)
                break

    def send_message(self, user, message):
        message += "\n"
        for connection in self.connections:
            if connection["user"] != user:
                print(message)
                connection["user"].send(message.encode())


if __name__ == "__main__":
    sock = socket.socket()
    server = Server()
    thread = threading.Thread(target=server.get_socket())
    thread.start()
    thread.join()