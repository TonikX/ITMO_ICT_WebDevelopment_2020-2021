import threading
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12345))
server.listen()

clients = []
addresses = []

def chat(client):
	while True:
		message = client.recv(4096)
		print(message)
		for client in clients:
			client.send(message)


def new_connection():
	while True:
		client, address = server.accept()
		print(f'{address} has connected')

		client.send('You are connected!'.encode('utf-8'))

		clients.append(client)
		addresses.append(address)

		thread = threading.Thread(target=chat, args=(client,))
		thread.start()

new_connection() 