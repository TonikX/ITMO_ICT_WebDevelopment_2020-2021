import socket

import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('localhost', 9090))

server.listen()

clients = []
nicknames = []


def broadcast(msg):
    for client in clients:
        client.send(msg)


def handle(client):
    while True:
        try:
            data = client.recv(1024)
            broadcast(data)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} left us(('.encode('ascii'))
            nicknames.remove(nickname)
            break


def receive():
    while True:
        client, adress = server.accept()
        print(f"Connected with {str(adress)}")

        client.send('name'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print(f'Nickname of the client is {nickname}')

        broadcast(f'{nickname} entered the chat '.encode('ascii'))
        client.send('Connected!'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


print('Server is waiting for connections...')
receive()