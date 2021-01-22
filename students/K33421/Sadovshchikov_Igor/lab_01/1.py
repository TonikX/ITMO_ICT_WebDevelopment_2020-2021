import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 4000))
server_socket.listen()

while True:
    print('Waiting for connection...')
    client_socket, addr = server_socket.accept()
    print('Connection from', addr)

    while True:
        request = client_socket.recv(4096)

        if request:

            if request == b'Hello, server\n':
                response = 'Hello, client\n'.encode()
                client_socket.send(response)
            else:
                response = 'I dont understand\n'.encode()
                client_socket.send(response)
