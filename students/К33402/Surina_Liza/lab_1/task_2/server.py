import socket
import pickle

BUFFER_SIZE = 4096

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(10)

conn, addr = sock.accept()

all_data = bytearray()
data = conn.recv(BUFFER_SIZE)

all_data += data

obj = pickle.loads(all_data)
print('Obj:', obj)
result = 0.5 * (obj['a'] + obj['b']) * obj['h']
print(result)
conn.send(str(result).encode())

conn.close()
