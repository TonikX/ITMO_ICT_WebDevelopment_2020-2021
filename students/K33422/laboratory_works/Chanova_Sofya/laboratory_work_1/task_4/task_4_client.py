import socket
import threading

nickname = input('please enter your nickname: ')

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 14042
client_socket.connect((host, port))


def receive_messages():  # получение сообщений или выбрать ник
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message == 'NICKNAME':
                client_socket.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print('error')
            client_socket.close()
            break


def send_message():  # отправить сообщение
    while True:
        message = f'{nickname}: {input("")}'
        client_socket.send(message.encode('utf-8'))


# поток получения сообщений
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

# поток отправки сообщений
send_thread = threading.Thread(target=send_message)
send_thread.start()



























