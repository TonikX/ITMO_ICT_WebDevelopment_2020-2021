import socket
import json

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 9090))


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


send_data("test")
data = receive_data()
sock.close()

print(data)
