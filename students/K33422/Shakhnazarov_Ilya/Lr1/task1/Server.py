import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(("localhost", 21002))
conn.listen(10)

while True:
    try:
        cl_sock, cl_addr = conn.accept()
        data = cl_sock.recv(1024)
        print(data.decode())
    except KeyboardInterrupt:
        conn.close()
        break