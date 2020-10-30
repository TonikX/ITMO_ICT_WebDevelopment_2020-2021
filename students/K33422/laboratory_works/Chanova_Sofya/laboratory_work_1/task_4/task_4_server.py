import socket
import threading

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 14042

server_socket.bind((host, port))
server_socket.listen(10)

clients = []
nicknames = []
print('starting chat server on: ', host, port, ' press ctrl+c to exit')


def broadcast(message):  # рассылка сообщения всем клиентам в чате
    for client in clients:
        client.send(message)


def handle_client(client):  # получить сообщение или выход из чата
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            client_index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[client_index]
            nicknames.remove(nickname)
            broadcast(f'{nickname} has left the chat'.encode('utf-8'))
            break


def receive():  # потоковое получение сообщений
    while True:
        client_socket, client_address = server_socket.accept()
        print(f'connected to: {client_address}')

        client_socket.send('NICKNAME'.encode('utf-8'))
        nickname = client_socket.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client_socket)

        print(f'nickname of the client is {nickname}')
        broadcast(f'{nickname} has entered the chat'.encode('utf-8'))
        client_socket.send('successful connection to the chat'.encode('utf-8'))

        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()


receive()

















