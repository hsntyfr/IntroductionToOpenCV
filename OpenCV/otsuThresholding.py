import cv2 as cv
import numpy as np

pic = cv.imread("pictures/solvay.png", 0)
ret, thresh1 =cv.threshold(pic, 120, 255, cv.THRESH_BINARY)
ret2, thresh2 = cv.threshold(pic, 0 ,255, cv.THRESH_BINARY + cv.THRESH_OTSU)



cv.imshow("original", pic)
cv.imshow("thresh1", thresh1)
cv.imshow("thresh2", thresh2)







cv.waitKey(0)
cv.destroyAllWindows