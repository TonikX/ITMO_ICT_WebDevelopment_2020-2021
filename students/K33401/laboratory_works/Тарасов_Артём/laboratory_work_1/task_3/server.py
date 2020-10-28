import socket
from threading import Thread
import threading


class Server:

    def __init__(self):
        sock.bind(('localhost', 9090))
        sock.listen(10)
        print("Server was started on socket:", sock)
        print("Wait for users...")

    def get_socket(self):
        while True:
            client, addr = sock.accept()
            clients.append({"connection": client, "socket": addr})
            print("connected:", addr)
            Thread(target=self.check_messages, args=(client,)).start()

    def check_messages(self, client):
        while True:
            try:
                data = client.recv(1024)
                self.target_cast(client, open("index.html").read())
            except Exception as ex:
                self.delete_user_socket(client)
                break

    def delete_user_socket(self, client):
        for user in clients:
            if user["connection"] == client:
                clients.remove(user)
                break

    def target_cast(self, client, message):
        headers = bytes(f'HTTP/1.0 200 OK\nContent-Type: text/html\n\n{message}', 'utf-8')
        # message += "\n"
        client.send(headers)


if __name__ == "__main__":
    sock = socket.socket()
    clients = []
    server = Server()
    thread = threading.Thread(target=server.get_socket())
    thread.start()
    thread.join()
