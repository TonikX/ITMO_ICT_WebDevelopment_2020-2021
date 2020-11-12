import socket
import threading

sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sckt.bind(('127.0.0.1', 9090))
sckt.listen(10)
users = set()


def connect_users():
    while True:
        clientsocket, addr = sckt.accept()
        users.add(clientsocket)
        print('connected:' + str(addr))
        threading.Thread(target=message, args=[clientsocket, addr]).start()


def message(clientsocket, addr):
    print('typing' + str(addr))
    while True:
        try:
            data = clientsocket.recv(1024)
            if not data:
                break
            for user in users:
                if user == clientsocket:
                    continue
                user.sendall(data)
        except Exception:
            users.remove(clientsocket)
            break
    print('left chat' + str(addr))
    clientsocket.close()


threading.Thread(target=connect_users()).start()
