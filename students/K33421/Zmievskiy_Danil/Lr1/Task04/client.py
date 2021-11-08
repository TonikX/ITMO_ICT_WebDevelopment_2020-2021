import socket
import threading

def chat():
     while True:
         data = conn.recv(1024)
         print(data.decode('utf-8'))

nickname = input()

conn = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
conn.connect(('', 7070))
conn.send(('Please welcome '+nickname).encode('utf-8'))

threading.Thread(target=chat).start()

while True:
	message = input()
	conn.send(('*'+nickname+'*: '+message).encode('utf-8'))