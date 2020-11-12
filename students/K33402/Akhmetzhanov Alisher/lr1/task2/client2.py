import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 9090))

parties = input("Please, Input size of parties a, b")

sock.send(parties.encode("UTF-8"))
data = sock.recv(1024)
print(data.decode("UTF-8"))
sock.close()

sock.close()
