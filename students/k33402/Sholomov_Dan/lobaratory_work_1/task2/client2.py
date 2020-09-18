import socket


def task2():
    sock = socket.socket()
    sock.connect(('localhost', 22222))
    print("Введите высоту и сторону параллелограмма через пробел:")
    sock.send(bytes(input(), "utf-8"))
    data = sock.recv(1024)
    sock.close()
    print(data.decode('utf-8'))


if __name__ == '__main__':
    task2()
