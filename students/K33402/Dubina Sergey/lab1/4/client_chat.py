import socket

import threading

nickname = input("Type your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('localhost', 9090))


def receive():
	while True:
		try:
			data = client.recv(1024).decode('ascii')
			if data == 'name':
				client.send(nickname.encode('ascii'))
			else:
				print(data)
		except:
			print("Shoto ne tak((")
			client.close()
			break

def write():
	while True:
		message = f'{nickname}: {input("")}'
		client.send(message.encode('ascii'))

receive_thread = threading.Thread(target = receive)
receive_thread.start()

write_thread = threading.Thread(target = write)
write_thread.start()