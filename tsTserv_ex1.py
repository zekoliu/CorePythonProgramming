
from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZE = 1024

ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('waiting for connect...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('...connect from: ', addr)

    while True:
        data = tcpCliSock.recv(BUFSIZE)
        print 'friend:  %s' % data
        send = raw_input('I: ')
        if not data and not send:
            break
        tcpCliSock.send('%s' % send)


tcpSerSock.close()