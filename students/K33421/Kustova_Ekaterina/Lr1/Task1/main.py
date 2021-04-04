import socket


# Задание №1
# СЕРВЕР

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.bind(('', 14900))
    sock.listen(1)
    conn, addr = sock.accept()
    data = conn.recv(16384)
    udata = data.decode("utf-8")
    print("Received message: " + udata)
    conn.send(b"Hello, client\n")
    conn.send(b"Your message: " + udata.encode("utf-8"))

    conn.close()


if __name__ == "__main__":
    main()
