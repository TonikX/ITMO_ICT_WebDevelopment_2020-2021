from socket import *
import sys

conn = socket(AF_INET, SOCK_STREAM)
conn.connect(("127.0.0.1", 14900))

print("We are going to solve quadratic equation: a*x^2 + b*x + c = 0")
a = input("Enter a: ")
b = input("Enter b: ")
c = input("Enter c: ")

if not a:
	conn.close()
	sys.exit(1)

data = str.encode(','.join([a,b,c]))
conn.send(data)

data = conn.recv(1024)
print(data.decode())

conn.close()
