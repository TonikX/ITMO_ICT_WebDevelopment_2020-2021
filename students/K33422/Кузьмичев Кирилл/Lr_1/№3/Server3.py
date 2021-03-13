import socket
import webbrowser

Sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Sock.bind(("127.0.0.3", 11042))
Sock.listen(1)
conn, addr = Sock.accept()

print('connected: ', addr)

while True:
    data = conn.recv(1024)
    if not data:
        break
    with open('index.html', 'rb') as file:
        html = file.read()
        conn.sendall(bytes(f'HTTP/1.1 200 OK\nContent-Type: text/html\n\n{html}', 'utf-8'))
        firefox_path = "C:\Program Files\Mozilla Firefox\firefox.exe"
        webbrowser.register('firefox', None, (webbrowser.BackgroundBrowser(firefox_path), 1))
        webbrowser.get(using ='firefox')
        webbrowser.open('index.html', new=2)

conn.close()