import socket
import threading
import time
import queue


class ClientHandler:
    def __init__(self, client_id, socket, addr, main_mailbox):
        super().__init__()
        self.client_id = client_id
        self.nickname = "Anonim"
        self.socket = socket
        self.addr = addr
        self.mailbox = queue.Queue()
        self.main_mailbox = main_mailbox

    def getSocket(self):
        return self.socket
  
    def getAddr(self):
        return self.addr
  
    def setNickname(self, nickname):
        self.nickname = nickname
    
    def getMailbox(self):
        return self.mailbox


class Message:
  def __init__(self, client_id, client_nickname, text):
    super().__init__()
    self.text = text
    self.isShared = False
    self.client_id = client_id
    self.client_nickname = client_nickname
  
  def getText(self):
    return self.text
  
  def setText(self, text):
    self.text = text
  
  def getClientId(self):
    return self.client_id
  
  def getClientNickname(self):
    return self.client_nickname


class History:
  def __init__(self):
    super().__init__()
    self.messages = []
  
  def isEmpty(self):
    return len(self.messages) == 0
  
  def addMessage(self, message):
    self.messages.append(message)
  
  def getFullHistory(self):
    return self.messages


class Server:
    def __init__(self, host, port):
        super().__init__()
        self.host = host
        self.port = port
        self.client_id_gen = 0
        self.clients = []
        self.history = History()
        self.mailbox = queue.Queue()


    def create_server_socket(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()


    def register_client(self, client):
        data = client.socket.recv(100)
        data = data.decode("UTF-8")
        client.nickname = data
        print("Клиент (id: {}) зарегистрирован: {}".format(client.client_id, client.nickname))


    def client_worker(self, client):
        print("Created client worker for client (id: {})".format(client.client_id))
        self.register_client(client)
        self.push_history(client)
        client.socket.setblocking(False)
        while True:
            try:
                chunk = client.socket.recv(100)
                if not chunk:
                    print("Клиент (id: {}) отключился".format(client.client_id))
                    return None
                message_text = chunk.decode("UTF-8")
                message = Message(client.client_id, client.nickname, message_text)
                print("Добавляем в историю...")
                client.main_mailbox.put(message)
            except socket.error:
                if not client.getMailbox().empty():
                    mail = client.getMailbox().get()
                    mail_text = mail.getText()
                    mail_sender = mail.getClientNickname()
                    mail_to_send = mail_sender + '|' + mail_text
                    print("Send to {}: {}".format(client.client_id, mail_to_send))
                    mail_to_send = mail_to_send.encode("UTF-8")
                    client.socket.sendall(mail_to_send)
                time.sleep(1)
  

    def push_history(self, client):
        print("Push history to (id: {} nickname: {})".format(client.client_id, client.nickname))
        for message in self.history.getFullHistory():
            message_text = message.getText()
            message_sender = message.getClientNickname()
            message_to_send = message_sender + '|' + message_text + ';'
            message_to_send = message_to_send.encode("UTF-8")
            client.socket.sendall(message_to_send)
        client.socket.sendall("/end".encode("UTF-8"))
          

    def run_server(self):
        print("Starting...")
        self.create_server_socket()
        print("Starting db_worker...")
        db_thread = threading.Thread(target=self.db_worker)
        db_thread.start()
        print("Serving...")
        try:
            while True:
                client_socket, client_addr = self.server_socket.accept()
                client = ClientHandler(self.client_id_gen, client_socket, client_addr, self.mailbox)
                self.clients.append(client)
                self.client_id_gen += 1
                print("Client (id: {}, addr: {}) connected".format(client.client_id, client.addr))
                t = threading.Thread(target=self.client_worker, args=(client, ))
                t.start()
        except KeyboardInterrupt:
            print("Stopping...")

        
    def db_worker(self):
        while True:
            if not self.mailbox.empty():
                message = self.mailbox.get()
                print("Main: get_mail: {}".format(message.getText()))
                self.history.addMessage(message)
                for client in self.clients:
                    client.getMailbox().put(message)


if __name__ == '__main__':
  server = Server("127.0.0.1", 3006)
  server.run_server()
