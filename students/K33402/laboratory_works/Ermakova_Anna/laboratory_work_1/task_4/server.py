import socket
import threading


def connection():
    while True:
        conn, addr = sock.accept()
        with clients_lock:
            clients.add(conn)
        print('connected ' + str(addr))
        threading.Thread(target=chat, args=[conn, addr]).start()


def chat(conn, addr):
    print('start chatting ' + str(addr))
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
    print('end chatting' + str(addr))
    conn.close()



sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
clients = set()
clients_lock = threading.Lock()
threading.Thread(target=connection).start()
