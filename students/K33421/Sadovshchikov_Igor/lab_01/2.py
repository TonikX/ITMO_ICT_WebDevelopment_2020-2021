import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 4000))
server_socket.listen()

def find_area(a: float, b:float , h:float) -> float:
    return (a+b)*h/2

def make_float(arr: list) -> list:
    return [float(i) for i in arr]

while True:
    client_socket, addr = server_socket.accept()
    print('Connection from', addr)
    client_socket.send('Connected. Send a, b and h.\n'.encode())

    while True:
        request = client_socket.recv(4096)

        if request:
            try:
                a,b,h = make_float(request.decode().split(' '))
                response = (str(find_area(a, b, h)) + '\n').encode()
                client_socket.send(response)
            except:
                client_socket.send('Unexpected input\n'.encode())
