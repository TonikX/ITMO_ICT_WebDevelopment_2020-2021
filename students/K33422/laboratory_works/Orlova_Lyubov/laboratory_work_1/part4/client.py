import socket
import threading
import time


name = input("What's your name? ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5555))

def receive():
	while True:
		try:
			message = client.recv(1024).decode('ascii')
			if message == 'new_conn':
				client.send(name.encode('ascii'))
			else:
				itsatime = time.strftime("%Y/%m/%d - %H:%M", time.localtime())
				print("[",itsatime,"] ", message)
		except:
			print("Server has stopped working!")
			client.close()
			break

def write():
	while True:
		message = f'{name}: {input("")}'
		client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()