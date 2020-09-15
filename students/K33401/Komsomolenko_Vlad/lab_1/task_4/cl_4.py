import socket
import time
from threading import Thread
import sys

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("127.0.0.1", 14903))
def receive():
	while True:
		data = conn.recv(16384)
		udata = data.decode("utf-8")
		if not data:
			break
		print(udata)

def send_mes():
	while True:
		message = input()
		if message:
			conn.send(bytes(message, "utf-8"))
		if message == "quit":
			sys.exit()
			break

receive_thread = Thread(target=receive)
send_thread = Thread(target=send_mes)
receive_thread.start()
send_thread.start()
send_thread.join()
receive_thread.join()
