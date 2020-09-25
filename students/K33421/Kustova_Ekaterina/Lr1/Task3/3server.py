import socket


# Задание №3
# СЕРВЕР
def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', 14900))
    sock.listen(1)
    conn, addr = sock.accept()
    while True:
        a = conn.recv(1024)
        a = a.decode("utf-8")
        print(a)
        page = open('index.html', 'r')
        content = page.read()
        conn.send(bytes(f'HTTP/1.0 200 OK\nContent-Type: content/page\n\n{content}', 'utf-8'))
        conn.close()
        break


if __name__ == "__main__":
    main()
