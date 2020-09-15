import socket

host = "127.0.0.1"
port = 9091

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

print("\nCalculating the area of a trapezoid\n")
data = input("Enter a, b, h (meters) separated by a space: ")
s.send(data.encode("utf-8"))

response = s.recv(16384)
print("Result: " + response.decode("utf-8") + " m")

s.close()