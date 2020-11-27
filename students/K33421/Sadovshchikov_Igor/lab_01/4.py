import socket
from select import select

"""
В словаре users будем хранить ондо значение сокета сервера и
пары сокет_клиента:адрес_клиента
"""
users = {}

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 4000))
server_socket.listen()


def new_connection(server_socket):

    conn, addr = server_socket.accept()
    ip_port = addr[0] + ':' + str(addr[1]) + ' '


    users[conn] = ip_port
    connected = list(users.keys())[1:]
    print(ip_port, 'connected.',
          f'Now {len(connected)} users in chat.')

    # Оповещаем пользователей о новом участнике
    for user in connected:
        user.send(ip_port.encode())
        user.send('connected!\n'.encode())

        if user == connected[-1]:
            user.send('Current users: \n'.encode())
            user.send((users[user]+'(You)').encode())
            user.send('\n'.encode())

            for sock in connected[:-1]:
                user.send(users[sock].encode())
                user.send('\n'.encode())
            user.send('\n'.encode())


def send_msg(conn):

    try:
        request = conn.recv(4096)

        if request:
            for user in users.keys():
                if user != server_socket and user != conn:
                    user.send(users[conn].encode())
                    user.send(request)

    except Exception as e:
        conn.close()

def event_loop():

    while True:
        to_monitor = users.keys()
        for conn in to_monitor:
            try:
                assert conn.fileno() != -1
            except AssertionError:

                disconnected = users[conn]
                users.pop(conn, None)

                # Сокеты подключенных пользователей (исключаем серверный сокет)
                connected = list(users.keys())[1:]
                print(disconnected, 'disconnected.', \
                      f'Now {len(connected)} users in chat.')

                # Оповещаем пользователей об отключившемся участнике
                for user in connected:
                    user.send(disconnected.encode())
                    user.send('disconnected!\n'.encode())
                break

        read_ready, _, _ = select(to_monitor, [], [])
        for conn in read_ready:

                if conn == server_socket:
                    new_connection(conn)
                else:
                    send_msg(conn)



if __name__ == '__main__':
    print('Started chat session.')
    users[server_socket] = ''
    event_loop()
