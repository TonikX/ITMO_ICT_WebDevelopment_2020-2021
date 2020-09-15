import socket
import time
import threading

def findID(client, clients, clientsocket):
	index = 0
	for client in clients:
		if client == clientsocket:
			break
		index += 1
	return index

def chat(clientsocket):
	while True:
		data = clientsocket.recv(16384)
		udata = data.decode("utf-8")
		if udata=='quit':
			clientsocket.close()
			index = findID(client, clients, clientsocket)
			del clients[index]
			all_index = findID(client, all_clients, clientsocket)
			all_index = str(all_index)
			print("Client is quit. Client's id: " + all_index)
			break
		else:
			for client in clients:
				if client is not clientsocket:
					index = str(findID(client, all_clients, clientsocket)).encode()
					client.send(b'id:' + index + b' '+ data)			

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(("127.0.0.1", 14903))
conn.listen(10)
clients = []
all_clients = []
while True:
	try:
		clientsocket, address = conn.accept()
		if clientsocket not in clients:
			clients.append(clientsocket)
			all_clients.append(clientsocket)
			print(clientsocket)
			my_thread = threading.Thread(target=chat, args=[clientsocket])
			my_thread.start()
	except socket.error:
		print('waiting clients')
		time.sleep(1)
	except KeyboardInterrupt:
		conn.close()
		break
