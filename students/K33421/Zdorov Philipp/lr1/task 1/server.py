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
        print(data)
    conn.send(b'Hello, client')

# Закрытие соединения
conn.close()
