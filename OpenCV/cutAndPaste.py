import cv2 as cv
import numpy as np

pic = cv.imread("pictures/logo.png")
pic2 = cv.imread("pictures/kizil.png")


section = pic[100:200, 300:400]
section2 = pic2[100:200, 200:300]
pic[100:200, 200:300] = section2

pic[300:400, 250:345] = (130, 140,170)
# pic[yParameter, xParameter] = (blue, green, red)

cv.imshow("picture", pic)





cv.waitKey(0)
cv.destroyAllWindows
