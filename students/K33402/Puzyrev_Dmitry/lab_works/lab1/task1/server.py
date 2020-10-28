from socketserver import *


class MyTCPHandler(StreamRequestHandler):
	def handle(self):
		self.data = self.request.recv(1024)
		print(str(self.data))

		self.request.sendall(b"Hello, client!")

if __name__ == "__main__":
	server = TCPServer(("127.0.0.1", 14900), MyTCPHandler)
	print("Starting server... for exit press Ctrl+C")
	server.serve_forever()
