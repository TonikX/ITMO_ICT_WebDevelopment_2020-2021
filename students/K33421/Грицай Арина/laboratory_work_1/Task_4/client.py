import socket
import threading

nickname = input("Choose your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 14902))


# подключаемся к серверу и посылаем ник
def receive():
    while True:
        try:
            message = client.recv(16384).decode('utf-8')
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print("Smth wrong!")
            client.close()
            break


# отправка сообщений на сервер
def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('utf-8'))


# запуск потоков для получения сообщений
receive_thread = threading.Thread(target=receive)
receive_thread.start()
# запуск потоков для отправки сообщений
write_thread = threading.Thread(target=write)
write_thread.start()
