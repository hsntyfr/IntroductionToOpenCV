import cv2 as cv
import numpy as np

pic = cv.imread("logo.png")
double = cv.pyrUp(pic)
halved = cv.pyrDown(pic)

print(pic.shape)
print(double.shape)
print(halved.shape)


cv.imshow("picture", pic)
cv.imshow("doubled", double)
cv.imshow("halved", halved)




cv.waitKey(0)
cv.destroyAllWindows