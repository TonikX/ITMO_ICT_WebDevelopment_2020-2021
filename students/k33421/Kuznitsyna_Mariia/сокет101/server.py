import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established")
    clientsocket.send(bytes("Hello, client!", "utf-8"))
    mesg = clientsocket.recv(1024)
    print(mesg.decode("utf-8"))
