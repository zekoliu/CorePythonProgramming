
from socket import *
from time import ctime

HOST = raw_input('Host: ')
PORT = raw_input('Port: ')
if HOST == '':
    HOST = 'localhost'
if PORT == '':
    PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = raw_input('I: ')
    if not data:
        break
    tcpCliSock.send(data)
    data = tcpCliSock.recv(BUFSIZE)
    if not data:
        break
    print'friend: %s ' % data

tcpCliSock.close()