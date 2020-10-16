import socket
import sys
from threading import Thread


def send_message(name):
	while True:
		text = input()
		sock.sendall((name + '__' + text).encode())
		if text == "exit":
			sock.close()
			sys.exit()

def receive_message():
	while True:
		data = sock.recv(1024)
		username = data.decode().split('__')[0]
		message = data.decode().split('__')[1].strip()
		print(f"{username}: {message}")


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 1235))

name = input("Username: ")
if not name:
	sock.close()
	sys.exit(1)

send_thread = Thread(target=send_message, args=[name])
get_thread = Thread(target=receive_message)

send_thread.start()
get_thread.start()