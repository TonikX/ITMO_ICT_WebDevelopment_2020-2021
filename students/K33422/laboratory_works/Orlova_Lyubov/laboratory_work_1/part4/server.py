import threading
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 5555))
server.listen()

clients = []
names = []
addresss = []

def broadcast(message):
	for client in clients:
		client.send(message)

def chat(client):
	while True:
		try:
			message = client.recv(1024)
			broadcast(message)
		except:
			index = clients.index(client)
			clients.remove(client)
			client.close()
			name = names[index]
			address = addresss[index]
			broadcast(f'{name} left the chat!'.encode('ascii'))
			print(f'Disconnected {address}')
			names.remove(name)
			addresss.remove(address)
			break

def new_connection():
	while True:
		client, address = server.accept()
		print(f"Connected with {str(address)}")

		client.send('new_conn'.encode('ascii'))
		name = client.recv(1024).decode('ascii')

		online = ""
		if len(names) == 0:
			online = "You are the only person in the chat"
		elif len(names) == 1:
			online = names[0]
			online += " is online!"

		else:
			for i, person in enumerate(names):
				online += f" {person}"
				if i != len(names) - 1:
					online += ","

			online += " are online!"


		names.append(name)
		clients.append(client)
		addresss.append(address)

		broadcast(f'{name} joined the chat!'.encode('ascii'))
		greeting = "Hi there! " + online
		client.send(greeting.encode('ascii'))

		thread = threading.Thread(target=chat, args=(client,))
		thread.start()

print("Server is listening...")
new_connection()