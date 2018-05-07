
from socket import *
import time

serverName = "123.207.77.222"
serverPort = 10001
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = 'kobe bryant'
for i in range(10):
    try:
        startTime = time.time()
        clientSocket.sendto(message, (serverName, serverPort))
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        print "run time is ", time.time() - startTime;
        print(modifiedMessage)
    except:
        print "Request timed out."
        continue
clientSocket.close()