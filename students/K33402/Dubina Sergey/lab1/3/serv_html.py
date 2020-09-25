import socket

print("Waiting for connections...")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 9090))
sock.listen()

n_sock, addr = sock.accept()
print("Client connected! Sending HTTP-message")



message = open("C:/index.html").read()
header = bytes(f'HTTP/1.0 200 OK\nContent-Type: text/html\n\n{message}', 'utf-8')
n_sock.send(header)

n_sock.close()


