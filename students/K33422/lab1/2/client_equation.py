import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 9090))


a = input("type symbol before x^2: ")
b = input("type symbol before x: ")
c = input("type 3 symbol: ")
q = f'{a}{b}{c}'

sock.send(bytes(q, "utf-8"))

data = sock.recv(1024)

print(f'ваш ответ: {data.decode("utf-8")}')