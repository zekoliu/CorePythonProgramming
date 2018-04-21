import numpy as np
import cv2

cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
img = cv2.imread('/home/jenenliu/Pictures/flower3.jpg',0)
cv2.imshow('image', img)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('messigray.png', img)
    cv2.destroyAllWindows()
