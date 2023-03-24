import cv2 as cv
import numpy as np

pic = cv.imread("pictures/kizil.png")
pic2 = cv.cvtColor(pic, cv.COLOR_BGR2GRAY) # = pic = cv.imread("kızıl.png", 0)
high, width, canalNumber = pic.shape
print("original picture", high, width,canalNumber)

# high2, width2, canalNumber2 = pic2.shape it is false because canal number is 0
high2, width2 = pic2.shape
print("grayed picture", high2, width2)


cv.imshow("grayed", pic2)









cv.waitKey(0)
cv.destroyAllWindows