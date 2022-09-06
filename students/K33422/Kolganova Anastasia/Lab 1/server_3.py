import socket
import json

binding_sock = socket.socket()
binding_sock.bind(('', 9090))
binding_sock.listen(1)
sock, address = binding_sock.accept()


def wrap_data(__data):
    return json.dumps({"data": __data}).encode("utf-8")


def unwrap_data(__data):
    if not __data:
        return False
    return json.loads(__data.decode("utf-8"))["data"]


def send_data(__data):
    sock.sendall(wrap_data(__data))


def receive_data():
    return unwrap_data(sock.recv(1024))


while True:
    data = receive_data()
    if not data:
        break

    with open('index.html', 'r') as file:
        html = file.read()

    reply = "HTTP/1.0 200 OK\n" + \
            "Content-Type: text/html\n\n" + \
            "{" +\
                html +\
            "}"
    send_data(reply)
sock.close()
