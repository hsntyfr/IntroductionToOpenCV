import cv2 as cv
import numpy as np

pic = cv.imread("pictures/solvay.png")

cv.rectangle(pic, (400, 300), (100, 450), [0, 0, 255], 3)
# (pic, bottom-left(x, y), top-right(x, y), rectangle color, border width)



cv.imshow("solvay", pic)








cv.waitKey(0)
cv.destroyAllWindows