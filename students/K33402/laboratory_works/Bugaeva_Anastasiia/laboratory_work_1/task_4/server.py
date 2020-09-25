import socket
import threading


def monitor_connection():
    while True:
        conn, addr = sock.accept()
        with clients_lock:
            clients.add(conn)
        print('Connected ' + str(addr))
        threading.Thread(target=chat, args=[conn, addr]).start()


def chat(conn, addr):
    print('Chat started ' + str(addr))
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            with clients_lock:
                for cl in clients:
                    if cl == conn:
                        continue
                    cl.sendall(data)
        except Exception as e:
            clients.remove(conn)
            break
    print('Chat ended ' + str(addr))
    conn.close()


if __name__ == '__main__':
    sock = socket.socket()
    sock.bind(('', 9090))
    sock.listen(1)
    clients = set()
    clients_lock = threading.Lock()
    threading.Thread(target=monitor_connection).start()