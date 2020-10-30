import socket

if __name__ == '__main__':
    sock = socket.socket()
    sock.connect(('localhost', 9090))
    sock.send(b'hello, server!')

    data = sock.recv(1024)
    sock.close()

    print(data.decode("utf-8"))
