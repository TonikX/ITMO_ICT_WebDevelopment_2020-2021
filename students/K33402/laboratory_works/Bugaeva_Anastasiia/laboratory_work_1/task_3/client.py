import socket

if __name__ == '__main__':
    sock = socket.socket()
    sock.connect(('localhost', 9090))

    while True:
        data = sock.recv(1024)
        if not data:
            break
        print(data.decode('utf-8'))
    sock.close()
