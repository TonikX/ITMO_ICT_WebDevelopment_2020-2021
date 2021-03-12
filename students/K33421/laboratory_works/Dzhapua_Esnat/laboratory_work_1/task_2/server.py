import socket
import math

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(("127.0.0.1", 14900))
conn.listen(10)

while True:
    try:
        clientsocket, adress = conn.accept()
        data = clientsocket.recv(16384)
        a,b,c = data.split()
        a = int(a)
        b = int(b)
        c = int(c)
        d = (b * b) - (4 * a * c)
        if d < 0:
            clientsocket.send(bytes("Нет корней"), "utf-8")
        if d == 0:
            x = str(-b+math.sqrt(d))/(2*a)
            clientsocket.send(bytes(x))
        else:
            x1 = str((-b+math.sqrt(d))/(2*a))
            x2 = str((-b-math.sqrt(d))/(2*a))

            clientsocket.send(bytes("X1 = "+x1+" X2 = "+x2, "utf-8"))

    except KeyboardInterrupt:
        conn.close()
        break
