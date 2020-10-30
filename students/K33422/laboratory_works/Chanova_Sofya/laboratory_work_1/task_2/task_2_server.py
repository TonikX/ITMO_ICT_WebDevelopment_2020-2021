import socket
import time
import struct

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 14003
server_socket.bind((host, port))
server_socket.listen(10)
server_socket.setblocking(False)

while True:
    try:
        client_socket, client_address = server_socket.accept()
        print(f'connected to: {client_address}')
        server_socket.setblocking(True)

        # получение данных об основаниях и высоте трапеции
        data = client_socket.recv(16384)
        data = struct.unpack('ddd', data)
        a = data[0]
        b = data[1]
        h = data[2]

        print('received first base: ' + str(a))
        print('received second base: ' + str(b))
        print('received height: ' + str(h))

        # расчет площади
        area = (a + b) / 2 * h
        area = struct.pack('d', area)

        client_socket.send(area)

        server_socket.close()
        break

    except socket.error:
        time.sleep(3)

    except KeyboardInterrupt:
        server_socket.close()
        break




