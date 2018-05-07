from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(1)
savelist = ['index.html', 'first.html', 'second.html', 'baidu.html']
print("The server is ready to receive")
while 1:
    connectSocket, addr = serverSocket.accept()
    sentence = connectSocket.recv(1024)
    print sentence
    sentence = sentence.split('\r\n')
    sentence = sentence[0].split()
    sentence = sentence[1].split('/')
    result = sentence[1]
    if result in savelist:
        connectSocket.send("HTTP/1.1 200 OK\r\n")
    else:
        connectSocket.send("HTTP/1.1 404 not find\r\n")
    connectSocket.close()