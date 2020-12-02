import socket
from threading import Thread
import sys

def send_msg():
	while True:
		msg = input()
		s.send(msg.encode('utf-8'))
		
		if msg == "bye":
			s.close()
			break
		

def receive_msg():
	while True:
		try:
			response = s.recv(16384)
			if response:
				print(response.decode('utf-8'))
		except OSError:	
			exit()

host = "127.0.0.1"
port = 9090
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

print("You connected to chat. Enter 'bye' to disconnect. ")
name = input("Enter your name: ")
s.send(name.encode('utf-8'))


sending = Thread(target = send_msg)
receiving = Thread(target = receive_msg)
sending.start()
receiving.start()
sending.join()
receiving.join()