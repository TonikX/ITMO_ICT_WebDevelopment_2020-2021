import socket
from threading import Thread


utf = "utf-8"
clients = []


def clients_in():
    while True:
        try:
            conn.setblocking(True)
            clientsocket,address = conn.accept()
            conn.setblocking(False)
            if clientsocket not in clients:
                clients.append((clientsocket, address))
                print(address, " connected to chat")

        except OSError:
            pass


def msg_in():
    while True:
        try:
            for client in clients:
                msg = client[0].recv(16348).decode(utf)
                print(client[1], " : "+msg)
                if msg == "bye":
                    client[0].close()
                    print(client[1], " has left the chat")
                    msg = f"User {client[1]} has left the chat"
                for clntout in clients:
                    if clntout[0] == clients[0]:
                        continue
                    data = f'User {client[1]}: '+msg
                    clntout[0].sendall(data.encode(utf))
        except OSError:
            pass


conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(("127.0.0.1", 19400))
conn.listen(10)
conn.setblocking(False)

clnthrd = Thread(target=clients_in)
msgthrd = Thread(target=msg_in)
clnthrd.start()
msgthrd.start()


