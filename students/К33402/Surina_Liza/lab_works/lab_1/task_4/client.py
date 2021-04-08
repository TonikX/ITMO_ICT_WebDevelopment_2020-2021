import socket
import sys

debug = True

conn = None
running = True

HOST = "localhost"
PORT = 9090
BUFSIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

while running:
    sendDat = input(">> ")
    line = "\n"
    sendData = "client: " + sendDat + line
    sock.send(bytes(sendData, 'utf-8'))
    if sendDat == "stop":
        sys.exit()

    recvData = sock.recv(BUFSIZE)
    print(recvData.decode())

sock.close()
