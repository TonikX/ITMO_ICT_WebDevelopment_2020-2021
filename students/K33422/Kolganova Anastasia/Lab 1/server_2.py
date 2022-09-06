import socket
import json
import math

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
    a = int(str(data).split()[0])
    b = int(str(data).split()[1])
    c = int(str(data).split()[2])
    D = b * b - 4 * a * c
    if D >= 0:
        if D == 0:
            result = -b // (2 * a)
            send_data(result)
        else:
            x1 = (-b + math.sqrt(D)) // (2 * a)
            x2 = (-b - math.sqrt(D)) // (2 * a)
            result = [x1, x2]
            send_data(result)
    else:
        send_data("D < 0, no equation roots")
        # parsedResult = json.loads(result)
sock.close()
