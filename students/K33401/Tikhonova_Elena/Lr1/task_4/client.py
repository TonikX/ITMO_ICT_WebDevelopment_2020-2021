import socket
import threading

def receive_messages(socket):
    try:
        while True:
            data = socket.recv(1024)
            print(data.decode("utf-8"), end='')
    except ConnectionAbortedError as e:
        print('Вы покинули чат')


if __name__ == "__main__":

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        s.connect(('localhost', 8080))

        data = s.recv(1024)
        print(data.decode("utf-8"))

        name = input().encode("utf-8")
        s.send(name)

        print('Print you messages...')
        print('q for quit. "." for update')

        x = threading.Thread(target=receive_messages, args=(s,))
        x.start()

        while True:
            message = input().encode("utf-8")
            if message == b'.':
                print("\r")
            s.send(message)
            if message == b'q':
                break