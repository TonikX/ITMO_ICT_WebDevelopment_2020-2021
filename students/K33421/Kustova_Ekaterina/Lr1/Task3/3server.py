import codecs
import socket


# Задание №3
# СЕРВЕР
def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("127.0.0.1", 14900))
    sock.listen(1)
    link = str('http://%s:%d' % ("127.0.0.1", 14900))

    while True:
        conn, addr = sock.accept()
        conn.sendall(link.encode('utf-8'))
        a = conn.recv(1024)
        a = a.decode("utf-8")
        print(a)
        response_type = 'HTTP/1.0 200 Ok\n'
        headers = 'Content-Type: text/html\n\n'
        body = codecs.open("index.html")
        response = response_type + headers + body.read()
        conn.sendall(response.encode('utf-8'))
        conn.close()


if __name__ == "__main__":
    main()
