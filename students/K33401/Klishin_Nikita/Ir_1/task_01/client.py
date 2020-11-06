import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("127.0.0.1", 3000))
conn.send(str.encode("Hell  o, server"))
response = conn.recv(1024).decode("UTF-8")
print("Server response: " + response)