
from socket import *

HOST = raw_input('Host: ')
PORT = raw_input('Port: ')
if HOST == '':
    HOST = 'localhost'
if PORT == '':
    PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = raw_input('> ')
    if not data:
        break
    udpCliSock.sendto(data, ADDR)
    data, ADDR = udpCliSock.recvfrom(BUFSIZE)
    if not data:
        break
    print data

udpCliSock.close()