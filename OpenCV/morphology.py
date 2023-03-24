import cv2 as cv
import numpy as np

pic = cv.imread("pictures/train.jpg")

kernel = np.ones((5, 5), np.uint8)

#dilation = cv.dilate(pic, kernel, iterations=1)
#eroison = cv.erode(pic, kernel, iterations=1)
#opening = cv.morphologyEx(pic, cv.MORPH_OPEN, kernel)
#closing = cv.morphologyEx(pic, cv.MORPH_CLOSE, kernel)
#gradian = cv.morphologyEx(pic, cv.MORPH_GRADIENT, kernel)
#tophat = cv.morphologyEx(pic, cv.MORPH_TOPHAT, kernel)
blackhat = cv.morphologyEx(pic, cv.MORPH_BLACKHAT, kernel)


#cv.imshow("dilation", dilation)
#cv.imshow("eroison", eroison)
#cv.imshow("opening", opening)
#cv.imshow("closing", closing)
#cv.imshow("gradian", gradian)
#cv.imshow("tophat", tophat)
cv.imshow("blackhat", blackhat)



cv.waitKey(0)
cv.destroyAllWindows()