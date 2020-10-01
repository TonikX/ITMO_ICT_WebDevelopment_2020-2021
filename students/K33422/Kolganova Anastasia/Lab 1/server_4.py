import socket

binding_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
binding_sock.bind(('', 9090))

# Массив где храним адреса клиентов
client = []
print('Start Server')
while True:
    # вернет данные и адрес сокета с которого получены эти данные
    sock, address = binding_sock.recvfrom(1024)
    print('Got ', sock[0], address[1])
    if address not in client:
        client.append(address)
    for clients in client:
        if clients == address:
            continue   # Не отправлять данные клиенту, который их прислал
        print("Sent data to clients")
        binding_sock.sendto(sock, clients)

