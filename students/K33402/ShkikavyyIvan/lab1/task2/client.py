import socket

sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sckt.connect(('localhost', 8080))

while True:
    try:
        data = sckt.recv(1024)
        if not data:
            sckt.close()
            break
        print(data.decode("utf-8"))
        sckt.sendall(bytes(input(), "utf-8"))
    except KeyboardInterrupt:
        sckt.close()
        break
