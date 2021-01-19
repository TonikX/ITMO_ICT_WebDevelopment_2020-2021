import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 7776))
sock.listen(1)
conn, addr = sock.accept()

while True:
    conn.send('I need the parallelogram`s base and height'.encode('utf-8'))
    try:
        data = conn.recv(1024)
        if not data:
            break
        if data.decode('utf-8') == 'exit':
            conn.close()
            break
        a, h = data.decode('utf-8').split(', ')
        s = (int(a) * int(h))
        print('S = ', s)
    except KeyboardInterrupt:
        conn.close()
        break

sock.close()