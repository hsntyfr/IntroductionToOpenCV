import cv2 as cv
import numpy as np

pic1 = cv.imread("pictures/logo.png")
pic2 = cv.imread("pictures/finger.png")
bitAnd = cv.bitwise_and(pic1, pic2)

cv.imshow("pic1", pic1)
cv.imshow("pic2", pic2)
cv.imshow("bitAnd", bitAnd)




cv.waitKey(0)
cv.destroyAllWindows()
