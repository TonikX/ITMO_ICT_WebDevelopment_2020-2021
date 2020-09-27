import socket
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    conn.connect(("127.0.0.1", 14900))
    conn.send(b"Hello, server\n")
    data = conn.recv(16384)
    udata = data.decode("utf-8")
    print(udata)
except ConnectionResetError as e:
    print('Сервер разорвал соединение, ваше сообщение не было получено')
finally:
    conn.close()
