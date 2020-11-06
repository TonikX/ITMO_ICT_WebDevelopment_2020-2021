import socket


print("Введите коэффициенты \n квадратного уравнения: ")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

request = " ".join(map(str, [a, b, c]))
request = request.encode("UTF-8")

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("127.0.0.1", 3000))
conn.send(request)
data = conn.recv(1024)
data = data.decode(encoding="UTF-8")
print(data)
