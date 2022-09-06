import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))
print("Введите длину первого основания")
a = input()
print("Введите длину второго основания")
b = input()
print("Введите длину высоты трапеции")
h = input()
s.sendall(bytes((str(a) + " " + str(b) + " " + str(h)), "utf-8"))

msg = s.recv(1024)
print(msg.decode("utf-8"))
