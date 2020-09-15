import socket
import threading


def client_thread(name, client_sock, clients):
	while True:
		try:
			msg = client_sock.recv(16384)

			if msg.decode('utf-8') == "bye":
				client_sock.close()
				delete_client_sock(client_sock, clients)
				for client in clients:
					client[1].send(b' --- ' + name + b' left the chat --- ')
			else:
				for client in clients:
					if (client[1]!=client_sock):
						client[1].send(name + b' > ' + msg)
		except OSError:
			pass


def delete_client_sock(client_sock, clients):
	for client in clients:
		if client[1] == client_sock:
			clients.remove(client)
			break


if __name__ == '__main__':
	host = "127.0.0.1"
	port = 9090
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((host, port))

	clients = []

	while True:
		try:
			s.listen()

			client_sock, client_addr = s.accept()
			name = client_sock.recv(1024)
			print("Connected client:", client_addr)
		
			clients.append((name, client_sock))
			
			for client in clients:
				if client[1]!=client_sock:
					client[1].send(b' --- ' + name + b' is connected to chat --- ')
			
			cl_thread = threading.Thread(target=client_thread, args=(name, client_sock, clients))
			cl_thread.start()


		except KeyboardInterrupt:
			s.close()
			break
