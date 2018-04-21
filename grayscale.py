import cv2
import numpy as np

img = cv2.imread('/home/jenenliu/Pictures/robot1.jpg')
print img.item(10, 10, 2)
img.itemset((10, 10, 2), 100)
print img.item(10, 10, 2)
print img.shape
print img.size
print img.dtype