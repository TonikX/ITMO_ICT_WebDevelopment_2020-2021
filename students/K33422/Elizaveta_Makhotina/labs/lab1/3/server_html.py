import socket

print("Waiting for connections...")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 9090))
sock.listen()

n_sock, addr = sock.accept()
print("Client connected! Sending HTTP-message")



conn.send(
    b"HTTP/1.0 200 OK\nContent-Type: text/html\n\n" + open("index.html", "rb").read()
)

n_sock.close()