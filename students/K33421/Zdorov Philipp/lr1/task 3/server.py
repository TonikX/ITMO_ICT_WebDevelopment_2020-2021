import socket
import sys

# Чтение html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

sock = socket.socket()

# Запуск на localhost на 9090 порту
sock.bind(('', 9090))

# Установка максимально допустимой очереди в 1 соединение
sock.listen(1)

# Открытие соединения
while True:
    try:
        conn, addr = sock.accept()
        # Отправка данных
        conn.send(f'HTTP/1.0 200 OK\nContent-Type: text/html\n{html}'.encode('utf-8'))
        # Получение данных
        data = conn.recv(1024)
        # Закрытие соединения
        conn.close()
    except KeyboardInterrupt:
        break
