import socket
import threading

debug = True
running = True

HOST = "localhost"
PORT = 9090
maxClient = 999
BUFSIZE = 1024

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind((HOST, PORT))
conn.listen(maxClient)

CONNS = []


def printed(aString):
    if debug:
        print(aString)


class talkToClient(threading.Thread):
    def __init__(self, clientSock, addr):
        self.clientSock = clientSock
        self.addr = addr
        threading.Thread.__init__(self)

    def run(self):
        while True:
            recvData = self.clientSock.recv(BUFSIZE)
            if recvData == "stop":
                break
            printed('Client ' + str(self.addr) + ' say "' + str(recvData) + '"')
            for c in CONNS:
                c.sendData(recvData)
        self.clientSock.close()

    def sendData(self, data):
        print('sending to ', self.addr)
        self.clientSock.send(data)


while running:
    printed('Running on ' + HOST + ': ' + str(PORT) + '.')
    channel, details = conn.accept()
    printed('Connect on : ' + str(details))
    CONNS.append(talkToClient(channel, details))
    print(CONNS)
    CONNS[-1].start()

conn.close()
