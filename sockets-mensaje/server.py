import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('localhost', 10000))

while True:
    data, address = sock.recvfrom(1024)
    print('received {} bytes from {} message {}'.format(len(data), address, data))