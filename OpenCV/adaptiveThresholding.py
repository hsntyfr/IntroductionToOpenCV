import cv2 as cv
import numpy as np

pic = cv.imread("pictures/finger.png", 0)
ret, thresh1 = cv.threshold(pic, 120, 255, cv.THRESH_BINARY)
#threshold function has to output first is boolean second is finished picture
thresh2 = cv.adaptiveThreshold(pic, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
thresh3 = cv.adaptiveThreshold(pic, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)




cv.imshow("original", pic)
cv.imshow("thresh1", thresh1)
cv.imshow("thresh2", thresh2)
cv.imshow("thresh3", thresh3)


cv.waitKey(0)
cv.destroyAllWindows