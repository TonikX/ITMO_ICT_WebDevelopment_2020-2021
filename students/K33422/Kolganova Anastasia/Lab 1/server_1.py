import socket

# создаем сокет
binding_sock = socket.socket()
# связываем сокет с хостом и портом
binding_sock.bind(('', 9090))
# запускаем режим прослушивания с максимальным
# количеством подключений в очереди 1
binding_sock.listen(1)
# принимаем подклюсение >> кортеж(новый сокет; адрес клиента)
sock, address = binding_sock.accept()

# порционное получение данных от клиента
while True:
    data = sock.recv(1024)
    if not data:
        break
    sock.send("Hello, client!".encode("utf-8"))
    print(data.decode("utf-8"))
sock.close()
