import socket
import threading

S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
S.bind(("127.0.0.2", 11042))
S.listen(3)
Account = []

def add_clients():
    while True:
        Sock, addr = S.accept()
        Account.append(Sock)
        threading.Thread(target = chat,  args = [Sock, addr]).start()

def chat(Sock, addr):
    print(addr)
    while True:
        try:
            feedback = Sock.recv(1024)
            if not feedback:
                break
            for client in Account:
                if client == Sock:
                    continue
                client.sendall(feedback)
        except Exception:
            Account.remove(Sock)
            break
    Sock.close()

threading.Thread(target=add_clients()).start()