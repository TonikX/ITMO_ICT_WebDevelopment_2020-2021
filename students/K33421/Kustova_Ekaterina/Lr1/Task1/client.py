import socket


# Задание №1
# КЛИЕНТ
def main():
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect(("127.0.0.1", 14901))
    conn.send(b"Hello, server \n")
    data = b""

    tmp = conn.recv(1024)
    while tmp:
        data += tmp
        tmp = conn.recv(1024)
    udata = (data.decode("utf-8"))
    print("Received message: " + udata)

    conn.close()


if __name__ == "__main__":
    main()
