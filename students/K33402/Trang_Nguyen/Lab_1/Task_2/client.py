import socket

HOST = socket.gethostname()
PORT = 1234
BUF_SIZE = 1024

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

server_msg = client.recv(BUF_SIZE)
print(server_msg.decode("UTF-8"))

# asks client to enter length of 2 sides of the right triangle
a = input("Enter the length of first side: ")
b = input("Enter the length of second side: ")

# sends input from client to server
client.send(str(a).encode())
client.send(str(b).encode())

# displays result to client
result = client.recv(1024)
if result:
    print(result.decode("UTF-8"))
else:
    print("Something went wrong. Please try again later!")

client.send(bytes("Thank you, server!", "UTF-8"))
client.close()