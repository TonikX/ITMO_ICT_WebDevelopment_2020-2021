import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(("127.0.0.1", 14900))
conn.listen(10)

while True:
    try:
        clientsocket,adress = conn.accept()
        html = open("index.html","r")
        data = html.read()
        response = "HTTP/1.0 200 OK\n"
        header = "Connect-Type: text/html\n"
        body = "".join(data)
        allfin = response + header + body
        clientsocket.send(allfin.encode("utf-8"))

    except KeyboardInterrupt:
        conn.close()
        break

