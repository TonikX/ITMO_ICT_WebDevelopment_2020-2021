import socket
import threading
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 1234))

nickname = input("Tell me your nickname ")
def receive():
    while True:
        try:
            msg = client.recv(1024).decode('utf-8')
            if msg == 'Give me a nickname123':
                client.send(nickname.encode('utf-8'))
            else:
                print(msg)
        except socket.error:
            time.sleep(5)
        except:
            client.close()
            break

def send():
    while True:
        msg = f'{nickname} : {input()}'
        client.send(msg.encode('utf-8'))


receive_thread = threading.Thread(target=receive)
send_thread = threading.Thread(target=send)
receive_thread.start()
send_thread.start()