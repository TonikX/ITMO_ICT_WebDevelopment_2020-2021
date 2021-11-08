import socket
import threading

nickname = input('Enter your name: ')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 9090))

def messages():
	while True:
		try:
			message = client.recv(1024).decode('utf-8')
			if message == 'NewUser':
				client.send(nickname.encode('utf-8'))
			else:
				print(message)
		except:
			client.close()
			break

def send_message():
	while True:
		message = f'{nickname}: {input("")}'
		client.send(message.encode('utf-8'))

recv_thread = threading.Thread(target=messages)
recv_thread.start()

send_thread = threading.Thread(target=send_message)
send_thread.start()