import socket


# Задание №2
# СЕРВЕР

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', 14900))
    sock.listen(1)
    conn, addr = sock.accept()

    while True:
        question = conn.recv(1024)
        question = question.decode("utf-8")
        print(question)
        data = conn.recv(1024)
        a, b, h = data.decode("utf-8").split(' ')
        s = ((int(a)+int(b)) / 2) * int(h)
        s = str(s)
        conn.send(b"Your result is " + s.encode("utf-8"))

        conn.close()
        break


if __name__ == "__main__":
    main()
