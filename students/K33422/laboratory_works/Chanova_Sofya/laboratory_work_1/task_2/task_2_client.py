import socket
import struct


def get_positive_float():  # получение данных в корректной форме
    while True:
        try:
            value = float(input())
        except ValueError:
            print("incorrect input. please enter a positive number")
            continue

        if value <= 0:
            print("incorrect input. please enter a positive number")
            continue
        else:
            break
    return value


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 14003))

# отправка данных о трапеции
print('send values to server to calculate area of trapezium: ')

print('first base: ')
a = get_positive_float()

print('second base: ')
b = get_positive_float()

print('height: ')
h = get_positive_float()

data = struct.pack('ddd', a, b, h)
client_socket.send(data)

# получение расчитанной площади
area = client_socket.recv(16384)
area = struct.unpack('d', area)
area = str(area[0])
print('trapezium area: ' + area)

client_socket.close()


