import threading
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("", 1234))
server.listen(20)

clients = []
nicknames = []
addresses = []

def chat(client):
    while True:
        try:
            msg = client.recv(1024)
            broadcast(msg)
        except socket.error:
            time.sleep(5)
        except KeyboardInterrupt:
            for client in clients:
                clients[0].close()
            break

def broadcast(msg):
    for client in clients:
        client.send(msg)

while True:
    client, address = server.accept()
    print(f"Have a connection with {address}")
    if client not in clients:
        clients.append(client)
        addresses.append(address)
        client.send('Give me a nickname123'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        broadcast(f"{nickname} joined!".encode('utf-8'))
    thread = threading.Thread(target=chat, args=(client,))
    thread.start()


