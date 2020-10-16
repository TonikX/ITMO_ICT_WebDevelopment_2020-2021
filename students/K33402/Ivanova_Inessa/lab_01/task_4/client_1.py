import socket
 import threading


 def send_message():
     try:
         while True:
             msg = input()
             sock.send(bytes(name + ": " + msg, 'utf-8'))
             if msg == 'bye':
                 sock.close()
                 break
     except Exception:
         pass
     finally:
         print('End chatting')


 def receive_message():
     try:
         while True:
             data = sock.recv(1024).decode('utf-8')
             if not data:
                 break
             print(data)
         sock.close()
     except Exception:
         pass


 if __name__ == '__main__':
     sock = socket.socket()
     sock.connect(('localhost', 9090))
     name = input('Enter your name\n')
     threading.Thread(target=send_message).start()
     threading.Thread(target=receive_message).start()