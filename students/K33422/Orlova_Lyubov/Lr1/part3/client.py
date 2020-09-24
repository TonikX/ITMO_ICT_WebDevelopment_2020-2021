import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 555))
msg = sock.recv(1024)
print(msg.decode("utf-8"))
sock.close()
