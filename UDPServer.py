from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The server is ready to recever")
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    print message
    modifiedMessage = message.upper()
    serverSocket.sendto(modifiedMessage, clientAddress)