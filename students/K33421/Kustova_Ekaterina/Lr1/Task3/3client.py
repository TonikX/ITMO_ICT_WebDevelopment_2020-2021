import socket


# Задание №3
# КЛИЕНТ

def main():
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect(("127.0.0.1", 14900))
    conn.send(b"Give me the page pls \n")
    a = conn.recv(1024)
    print(a.decode("utf-8"))

    conn.close()


if __name__ == "__main__":
    main()
