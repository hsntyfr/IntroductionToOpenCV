import cv2 as cv
import numpy as np

cam = cv.VideoCapture(0)

while True:
    ret, video = cam.read()
    cv.rectangle(video, (100, 100), (200, 200), (100, 150, 200), 5)
    cv.line(video, (50, 50), (250, 200), (50, 100, 150), 3)
    cv.circle(video, (500, 575), 100, (75, 150, 225), 8)
    cv.putText(video, "BANNED", (350, 450), cv.FONT_HERSHEY_PLAIN, 1, (65, 130, 195), 2)

    cv.imshow("video", video)
    if cv.waitKey(25) & 0xFF == ord('q'):
        break

cam.release()
cv.destroyAllWindows
