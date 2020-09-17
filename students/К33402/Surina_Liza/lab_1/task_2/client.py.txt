import socket
import pickle

conn = socket.socket()
conn.connect(('localhost', 9090))

obj = {
    'a': int(input("основание а = ")),
    'b': int(input("основание b = ")),
    'h': int(input("высота h = "))
}

data = pickle.dumps(obj)

conn.sendall(data)

da = conn.recv(4096)
msg = da.decode()
print("Площадь трапеции равна: " + msg)

conn.close()

