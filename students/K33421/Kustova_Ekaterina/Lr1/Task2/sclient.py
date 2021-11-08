import socket


# Задание №2
# КЛИЕНТ
def main():
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect(("127.0.0.1", 14900))

    question = "What is the area of a trapezoid?"
    conn.send(question.encode("utf-8"))
    data = input()
    conn.send(data.encode("utf-8"))
    result = conn.recv(1024)
    print(result.decode("utf-8"))

    conn.close()


if __name__ == "__main__":
    main()
