import socket

sock = socket.socket()

# Запуск на localhost на 9090 порту
sock.bind(('', 9090))

# Установка максимально допустимой очереди в 1 соединение
sock.listen(1)

# Открытие соединения
conn, addr = sock.accept()
while True:
    # Принятие 1024 байт сообщения
    data = conn.recv(1024)

    # Если данные прекратили поступать, закончить прием
    if not data:
        break
    # Иначе, напечатать данные
    else:
        data = data.decode().split()
        try:
            data = [float(d) for d in data]
        except TypeError:
            conn.send(f'Неправильно введены параметры'.encode())

        if len(data) != 3:
            conn.send(f'Неправильно введены параметры'.encode())
        if not data[2] and data[0] and data[1]:
            conn.send(f'Гиппотенуза: {(data[0] ** 2 + data[1]) ** 0.5}'.encode())
        elif (data[0] and not data[1]) or (data[1] and not data[0]):
            conn.send(f'Катет: {(data[2] ** 2 - max(data[0], data[1]) ** 2) ** 0.5}'.encode())
        else:
            conn.send(f'Неправильно введены параметры'.encode())

# Закрытие соединения
conn.close()
