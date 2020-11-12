import socket


def task1():
    sock = socket.socket()
    sock.connect(('localhost', 11111))
    sock.send(bytes('Hello, server', "utf-8"))
    data = sock.recv(1024)
    sock.close()
    print(data.decode('utf-8'))


if __name__ == '__main__':
    task1()
