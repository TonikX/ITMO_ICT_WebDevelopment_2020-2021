import socket

sock = socket.socket()
sock.connect(('localhost', 9090))

legs = input('Enter 2 legs: ')
sock.sendall(legs.encode('utf-8'))

data = sock.recv(1024)
sock.close()

print('Hypotenuse: ', data.decode('utf-8'))
