import socket

sock = socket.socket()

# Подключение к localhost на порту 9090
sock.connect(('localhost', 9090))

# отправка данных
sock.send(b'hello, server!')

# Принятие 1024 байт сообщения
data = sock.recv(1024)
print(data)

# Закрыть подключение
sock.close()
