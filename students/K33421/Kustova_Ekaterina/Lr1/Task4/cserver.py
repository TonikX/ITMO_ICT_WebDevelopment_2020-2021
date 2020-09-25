import socket
import threading

# Задание №4
# СЕРВЕР

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 14900))
sock.listen(3)
clients = []


def add_clients():
    while True:
        conn, addr = sock.accept()
        clients.append(conn)
        threading.Thread(target=chat, args=[conn, addr]).start()


def chat(conn, addr):
    print(str(addr))
    while True:
        try:
            a = conn.recv(1024)
            if not a:
                break
            for client in clients:
                if client == conn:
                    continue
                client.sendall(a)
        except Exception:
            clients.remove(conn)
            break
    conn.close()


threading.Thread(target=add_clients()).start()
