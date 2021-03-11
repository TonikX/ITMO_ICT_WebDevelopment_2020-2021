import socket

host = "127.0.0.1"
port = 9091

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

print("\nПоиск площади ттрапеции\n")
data = input("Введите a, b, h (в метрах) разделенные пробелом: ")
s.send(data.encode("utf-8"))

response = s.recv(16384)
print("Result: " + response.decode("utf-8") + " m")

s.close()