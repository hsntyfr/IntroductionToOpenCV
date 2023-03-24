import cv2 as cv
import numpy as np

pic = cv.imread("pictures/logo.png")

pic[100:200, :, 0] = 255

cv.imshow("picture", pic)

cv.waitKey(0)
cv.destroyAllWindows