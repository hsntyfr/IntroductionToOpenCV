import cv2 as cv
import numpy as np

pic = cv.imread("pictures/kizil.png")

# mirrored = cv.copyMakeBorder(pic, 300, 300, 300, 300, cv.BORDER_REFLECT)
# cv.copyMakeBorder(source, top, bottom, left, right, effect name)
# elongated = cv.copyMakeBorder(pic, 320, 320, 320, 320, cv.BORDER_REPLICATE)
# replicated = cv.copyMakeBorder(pic, 300, 300, 300, 300, cv.BORDER_WRAP)
# covered = cv.copyMakeBorder(pic, 300, 300, 300, 300, cv.BORDER_CONSTANT, value = (200, 150, 100))


# cv.imshow("picture", pic)
# cv.imshow("mirrored", mirrored)
# cv.imshow("elongated", elongated)
# cv.imshow("replicated", replicated)
# cv.imshow("covered", covered)








cv.waitKey(0)
cv.destroyAllWindows