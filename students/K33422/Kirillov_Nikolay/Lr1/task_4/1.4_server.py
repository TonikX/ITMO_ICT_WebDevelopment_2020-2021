import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 9090))
client = []
print('Server start')
while True:
    data, address = sock.recvfrom(1024)
    print('Got connection from: ', address[0], address[1])
    if address not in client:
        client.append(address)
    for clients in client:
        if clients == address:
            continue
        sock.sendto(data, clients)
