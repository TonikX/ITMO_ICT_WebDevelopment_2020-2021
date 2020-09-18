import socket


def task3():
    sock = socket.socket()
    sock.connect(('localhost', 33333))
    sock.send(bytes('.', "utf-8"))
    data = sock.recv(1024)
    sock.close()
    print(data.decode('utf-8'))


if __name__ == '__main__':
    task3()
