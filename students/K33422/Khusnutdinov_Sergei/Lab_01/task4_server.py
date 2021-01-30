import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 9090))
server.listen(10)

clients = []
nicknames = []

def broadcast(message):
	for client in clients:
		client.send(message)

def chat_messages(client):
	while True:
		try:
			message = client.recv(1024)
			broadcast(message)
		except:
			client_id = clients.index(client)
			clients.remove(client)
			client.close()
			disc_nickname = nicknames[client_id]
			nicknames.remove(disc_nickname)
			broadcast(f'{disc_nickname} has disconnected'.encode('utf-8'))
			break

def chatting():
	while True:
		conn, addr = server.accept()
		print('Connected: ', addr)

		conn.send('NewUser'.encode('utf-8'))
		nickname = conn.recv(1024).decode('utf-8')
		nicknames.append(nickname)
		clients.append(conn)

		broadcast(f'{nickname} has connected ....'.encode('utf-8'))
		conn.send('You have conencted to the chat'.encode('utf-8'))

		thread = threading.Thread(target=chat_messages, args=(conn,))
		thread.start()

chatting()