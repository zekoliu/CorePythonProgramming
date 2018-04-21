import sys
from pyzbar.pyzbar import decode
import cv2

if len(sys.argv) < 2:
    print("Usage: %s <image file>" % sys.argv[0])
    sys.exit(1)

filepath = sys.argv[1]
image = cv2.imread('/home/jenenliu/Desktop/wechat.jpg')
result = decode(image)
for item in result:
    print(item.type, item.data)

    # import threading
#
# class A(threading.Thread):
#     def __init__(self):
#         threading.Thread.__init__(self)
#     def run(self):
#         for i in range(10):
#             print('I am threading one')
#
# class B(threading.Thread):
#     def __init__(self):
#         threading.Thread.__init__(self)
#
#     def run(self):
#         for i in range(10):
#             print('I am threading two')
#
# a = A()
# b = B()
# a.start()
# b.start()