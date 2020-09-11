"""Server for multithreaded (asynchronous) chat application."""
import socket
import threading
import sys
import time


clients = {}
addresses = {}


HOST = socket.gethostname()
PORT = 1234
BUF_SIZE = 1024


def handle_client(client):  # Takes client socket as argument.
    """Handles a single client connection."""

    name = client.recv(BUF_SIZE).decode("UTF-8")
    clients[client] = name
    welcome = 'Welcome %s! Enter `q` anytime to exit.' % name

    client.send(bytes(welcome, "UTF-8"))
    msg = "%s has joined the chat!" % name
    broadcast(bytes(msg, "UTF-8"), client)

    while True:
        msg = client.recv(BUF_SIZE)
        if msg != bytes("q", "UTF-8"):
            broadcast(msg, client, name + ": ")
        else:
            print("%s:%s is offline" % addresses[client])
            client.send(bytes("You have left the chat! Now you cannot send message to people.", "UTF-8"))
            client.close()
            del clients[client]
            broadcast(bytes("%s has left the chat." % name, "UTF-8"))
            break


def broadcast(msg, client=None, prefix=""):  # prefix is for name identification.
    """Broadcasts a message to all the clients."""

    for sock in clients:
        if sock != client:
            sock.send(bytes(prefix, "UTF-8") + msg) 


if __name__ == "__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        server.bind((HOST, PORT))
    except Exception as msg:
        print("Socket Error: %s" % msg)
        sys.exit()

    server.listen(10)
    print("Waiting for connection...")

    # Sets up handling for incoming clients
    while True:
        client, client_address = server.accept()

        print("%s:%s has connected" % client_address)
        client.send(bytes("Hey! To start chatting, enter a nickname:", "UTF-8"))
        addresses[client] = client_address

        threading.Thread(target=handle_client, args=(client, )).start()
    
    sys.exit()