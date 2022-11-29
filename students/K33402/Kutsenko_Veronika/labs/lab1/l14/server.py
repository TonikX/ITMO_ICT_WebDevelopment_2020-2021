import socket

s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 9090))

connections = []

while 1:
    data, addres = s.recvfrom(1024)
    print(addres[0], addres[1])
    if addres not in connections:
        connections.append(addres)
    for client in connections:
        if client == addres:
            continue
        s.sendto(data, client)