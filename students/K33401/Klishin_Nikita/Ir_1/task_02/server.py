import socket
import math

HOST = "127.0.0.1"
PORT = 3000

print("Starting...")
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(10)

print("Work...")
while True:
    try:
        # создание серверного сокета
        client_socket, client_addr = server_socket.accept()
        data = client_socket.recv(1024)
        data = data.decode(encoding="UTF-8")
        result = str()
        a, b, c = map(float, data.split(' '))
        d = b**2 - 4*a*c
        if d < 0:
            result = "Нет корней"
        elif d == 0:
            x_1_2 = -b / (2 * a)
            result = "Один корень: " + str(x_1_2)
        else:
            x_1 = (-b - math.sqrt(d)) / (2 * a)
            x_2 = (-b + math.sqrt(d)) / (2 * a)
            result = "Два корня: " + str(x_1) + ' ' + str(x_2)
        result = result.encode(encoding="UTF-8")
        client_socket.sendall(result)
    except socket.error:
        client_socket.close()
    except KeyboardInterrupt:
        print("Stopping...")
        break