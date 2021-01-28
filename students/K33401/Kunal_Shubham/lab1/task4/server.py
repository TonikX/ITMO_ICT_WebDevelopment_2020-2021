import asyncio
import socket

clients = []

async def handle_client(client, address):
    data = f"Please welcome our new chat member from {address}"

    for _client in clients:
        await loop.sock_sendall(_client, data.encode('utf8'))

    while data != 'BYEBYE':
        data = (await loop.sock_recv(client, 1024)).decode('utf8')
        message = f'From {address}: ' + str(data)
        if data == 'BYEBYE':
            message = f'User {address} has left the chat'
        for _client in clients:
            if _client == client:
                continue
            await loop.sock_sendall(_client, message.encode('utf8'))
    clients.remove(client)
    print(f'Client: {address} disconnected')
    client.close()


async def run_server():
    while True:
        client, address = await loop.sock_accept(server)
        if client not in clients:
            clients.append(client)
        print(f'Client with address {address} connected to the chat!')
        loop.create_task(handle_client(client, address))


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 1337))
server.listen(8)
server.setblocking(False)
loop = asyncio.get_event_loop()
loop.run_until_complete(run_server())
