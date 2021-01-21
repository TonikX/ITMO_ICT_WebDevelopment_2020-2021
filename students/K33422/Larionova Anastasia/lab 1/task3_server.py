import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 7775
sock.bind((host, port))
sock.listen(1)
conn, addr = sock.accept()

print('The WEB server URL for this would be http://%s:%d/' % (host, port))
while True:
    with open('index.html', 'r') as file:
        response_type = 'HTTP/1.0 200 OK\n'
        headers = 'Content-Type: text/html\n\n'
        body = file.read()
        response = response_type + headers + body
        conn.send(response.encode('utf-8'))
    data = conn.recv(1024)
    if not data:
        break

conn.close()