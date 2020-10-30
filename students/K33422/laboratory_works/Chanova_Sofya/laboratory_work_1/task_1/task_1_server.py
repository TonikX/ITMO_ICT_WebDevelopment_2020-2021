import socket
import time

# сокет сервера
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 14000))
server_socket.listen(10)
server_socket.setblocking(False)

while True:
    try:
        # подключение к сокету клиента
        client_socket, client_address = server_socket.accept()
        print(f'connected to: {client_address}')
        server_socket.setblocking(True)

        # получение сообщения от клиента
        data = client_socket.recv(16384)
        data = data.decode('utf-8')
        print('received data: ' + data)

        # отправка сообщения клиенту
        server_msg = 'hello, client!'
        client_socket.send(bytes(server_msg, 'utf-8'))

        server_socket.close()
        break

    except socket.error:
        time.sleep(5)

    except KeyboardInterrupt:
        server_socket.close()
        break




