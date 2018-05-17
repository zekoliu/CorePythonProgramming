import os
import time

def getFileSize(filepath):
    temp = 0;
    while (1):
        fileSize = os.path.getsize(filepath)
        if (fileSize >= temp):
            print("Current file size is ", fileSize, ", this file increase size is ", fileSize - temp)
        else:
            print("Currnet file size is", fileSize,  ", this file reduce size is ", temp - fileSize)
        temp = fileSize
        time.sleep(60)

if __name__ == "__main__":
    getFileSize("/home/jenenliu/Desktop/test.txt")