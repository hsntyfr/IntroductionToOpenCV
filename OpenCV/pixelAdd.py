import cv2 as cv
import numpy as np

pic = cv.imread("pictures/kizil.png")
pic2 = cv.imread("pictures/logo.png")


print(pic[550, 750])
print(pic2[600, 600])


exit(0)
cv.waitKey(0)
cv.destroyAllWindows