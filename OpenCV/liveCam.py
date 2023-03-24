import cv2 as cv
import numpy as np

cam = cv.VideoCapture(0)
# if argument is 0 cam is itself
# if argument is 1 cam is usb camera
# if argument is 2 cam is video uploaded by user


while True:
    ret, picture = cam.read()
    # ret is boolean variable it returns if camera available it returns true
    cv.imshow("video", picture)
    if cv.waitKey(30) & 0xFF == ord('q'):
        break

cam.release()

cv.destroyAllWindows
