import socket
import json
from math import sin

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(("127.0.0.1", 14900))
conn.listen(10)

clientsocket, address = conn.accept()
clientsocket.send(b"""Hello, client
    \rPlease tell me everything you know about your parallelogram
    \r0 for field you don't know""")
data = clientsocket.recv(16384).decode("utf-8")
paral_info = json.loads(data)
result = [0,0,0]
result[0] = paral_info['a']*paral_info['a_h']
result[1] = paral_info['b']*paral_info['b_h']
result[2] = paral_info['a']*paral_info['b']*sin(paral_info['alpha'])
for res in result:
    if res != 0:
        clientsocket.send(("Площадь параллелограмма = "+str(res)).encode("utf-8"))
        conn.close()
try:
    clientsocket.send("Данных недостаточно, чтобы посчитать площадь параллелограмма".encode("utf-8"))
except Error as e:
    pass
finally:
    conn.close()