import cv2 as cv
import numpy as np

# there are have to equal pixel number

pic = cv.imread("pictures/manzara.png")
pic2 = cv.imread("pictures/uzay.png")

# add = cv.add(pic, pic2)
weightedAdd = cv.addWeighted(pic, 0.3, pic2, 0.7, 0)
# addWeighted(picture, ratio for first picture, picture, ratio for picture, 0 as default)

# cv.imshow("added", add)
cv.imshow("weighted", weightedAdd)










cv.waitKey(0)
cv.destroyAllWindows
