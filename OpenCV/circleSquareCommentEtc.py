import cv2 as cv
import numpy as np

pic = np.zeros((300, 300, 3), dtype="uint8")

cv.line(pic, (0, 0), (100, 100), (125, 222, 99), 5)
# cv.line(picture, (start x, start y), (finish x, finish y), (line color bgr), border width)

cv.circle(pic, (150, 150), 50, (190, 120, 100), 9)
# cv.circle(picture, (center x, center y), radius, (color), width)

cv.putText(pic, "HSN", (200, 200), cv.FONT_HERSHEY_COMPLEX, 1, (125, 250, 175), 1)
# cv.putText(picture, "text", (start x, start y), font type, text size, color, width)


cv.imshow("picture", pic)


cv.waitKey(0)
cv.destroyAllWindows