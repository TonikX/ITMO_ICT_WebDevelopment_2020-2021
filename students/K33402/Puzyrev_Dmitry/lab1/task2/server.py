from socketserver import *
import math

class MyTCPHandler(StreamRequestHandler):
  def handle(self):
    self.data = self.request.recv(1024)

    a = int(self.data.decode().split(",")[0])
    b = int(self.data.decode().split(",")[1])
    c = int(self.data.decode().split(",")[2])

    d = (b**2) - (4*a*c)
    sol1 = (-b-math.sqrt(d))/(2*a)
    sol2 = (-b+math.sqrt(d))/(2*a)

    result = "Solution 1: " + str(sol1) + "\n" + "Solution 2: " + str(sol2)
    self.request.sendall(result.encode())

if __name__ == "__main__":
	server = TCPServer(("127.0.0.1", 14900), MyTCPHandler)
	print("Starting server... for exit press Ctrl+C")
	server.serve_forever()



