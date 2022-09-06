import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established")
    mesg = clientsocket.recv(1024)
    a, b, h = mesg.decode("utf-8").split(' ')
    s = (int(a) + int(b)) * int(h) / 2
    clientsocket.send(bytes(f"Площадь трапеции равна {s} условных единиц", "utf-8"))

