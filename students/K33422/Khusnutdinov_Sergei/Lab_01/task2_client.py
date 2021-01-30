import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 9090))

print("Please, input only 'a', 'b' and 'c' from your quadratic equation sepparating them by space: ")
client.send(input().encode('utf-8'))

data = client.recv(1024)
print(data.decode('utf-8'))

client.close()