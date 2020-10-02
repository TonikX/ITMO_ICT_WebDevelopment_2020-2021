import socket
import threading

conn = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
conn.bind (('', 7070))
conn.listen()

clients = []

print ('Start Server')

def new_client():
	while True:
		clientsocket, address = conn.accept()
		if  clientsocket not in clients:
			clients.append(clientsocket)
		threading.Thread(target = chat,  args = [clientsocket, address]).start()

def chat(clientsocket, address):
	print (address[0], address[1])
	while True:
		try:
			data = clientsocket.recv(1024)
			
			for client in clients:
				if client == clientsocket:
					continue
				client.send(data)
		except Exception:
			clients.remove(clientsocket)

	clientsocket.close()

threading.Thread(target=new_client()).start()