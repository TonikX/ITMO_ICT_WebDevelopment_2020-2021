import socket

# сокет клиента
client_socket = socket.socket(socket.AF_INET,
                              socket.SOCK_STREAM)

client_socket.connect(('localhost', 14000))

# отправка сообщения серверу
client_msg = 'hello, server!'
client_socket.send(bytes(client_msg, 'utf-8'))

# получение сообщения от сервера
data = client_socket.recv(16384)
data = data.decode('utf-8')
print('received data: ' + data)

client_socket.close()



