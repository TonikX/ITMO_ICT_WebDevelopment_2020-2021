import socket

s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
s.connect((socket.gethostname(), 9090))

msg = s.recv(1024)
print(msg.decode("utf-8"))
leg1, leg2 = input("Введите стороны треугольника: ").split()
s.send(bytes(f"{leg1},{leg2}", "utf-8"))
print(s.recv(1024).decode("utf-8"))
s.close()