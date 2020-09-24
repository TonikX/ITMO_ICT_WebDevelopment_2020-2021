import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(("127.0.0.1", 14900))
conn.listen(10)

while True:
    try:
        clientsocket, adress = conn.accept()
        data = clientsocket.recv(16384)
        udata = data.decode("utf-8")
        print(udata)

        data2 = "Hello, client"
        clientsocket.send(bytes(data2,"utf-8"))

    except KeyboardInterrupt:
        conn.close()
        break



