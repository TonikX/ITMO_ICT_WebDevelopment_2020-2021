import socket
import threading

def get_connect(socket, number):
    print("I am thread number", number)
    clientsocket, address = socket.accept()
    clientsocket.send(b'Please enter your name: ')
    name = clientsocket.recv(1024)
    name = name.decode("utf-8")

    messages[name] = []

    print(name, 'is connected')
    while True:
        data = clientsocket.recv(1024)
        if data == b'q':
            print(name, 'left the chat')
            break
        else:
            if data != b'.':
                message = name + ':' + data.decode("utf-8")
                print(message)
                for key in messages:
                    if key != name:
                        messages[key].append(message.encode("utf-8"))
            while True:
                if bool(messages[name]):
                    clientsocket.send(messages[name].pop(0)+b'\n')
                else:
                    break

if __name__ == "__main__":

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('localhost', 8080))
        s.listen(10)
        messages = {}
        messages['all'] = []
        threads = []
        for i in range(3):    
            x = threading.Thread(target=get_connect, args=(s,i+1,))
            threads.append(x)
            x.start()
        for i in range(3):
            threads[i].join()
        #print(messages['all'])
