import cv2 as cv
import numpy as np

pic = cv.imread("pictures/kizil.png")
gray = cv.cvtColor(pic, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray, (3, 3), 0)

def autoCanny(blur, sigma = 0.33):
    median = np.median(blur)
    lower = int(max(0, (1 - sigma) * median))
    upper = int(min(255, (1 + sigma) * median))
    canny = cv.Canny(blur, lower, upper)
    return canny

wide = cv.Canny(blur, 10, 220)
tight = cv.Canny(blur, 200, 230)
auto = autoCanny(blur)

#canny = cv.Canny(blur, 50, 150)
#cv.imshow("blurred", blur)
#cv.imshow("canny", canny)

cv.imshow("edge", np.hstack((wide, tight, auto)))

cv.waitKey(0)
cv.destroyAllWindows
