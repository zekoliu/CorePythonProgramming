
from socket import *
from time import ctime

HOST = ''
PORT = 21567
ADDR = (HOST, PORT)
BUFSIZE = 1024

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print 'waiting from message...'
    data, addr = udpSerSock.recvfrom(BUFSIZE)
    udpSerSock.sendto('[%s] %s' % (ctime(), data), addr)
    print '...received from and returned to: ', addr

udpSerSock.close()