import socket

sock = socket.socket()

# Подключение к localhost на порту 9090
sock.connect(('localhost', 9090))

print('Введите данные в следующем формате:')
print('На месте искомой стороны треугольника введите 0')
data_send = input('<Катет> <Катет> <Гиппотенуза>').encode()

# отправка данных
sock.send(data_send)

# Принятие 1024 байт сообщения
data_receive = sock.recv(1024).decode()
print(data_receive)

# Закрыть подключение
sock.close()
