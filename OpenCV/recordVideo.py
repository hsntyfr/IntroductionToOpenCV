import cv2 as cv

cam = cv.VideoCapture(0)

width = int(cam.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(cam.get(cv.CAP_PROP_FRAME_HEIGHT))

print(width, height)

fourcc = cv.VideoWriter_fourcc(*'MP4V')

writer = cv.VideoWriter("video.mp4", fourcc, 20, (width, height))

while True:
    rte, frame = cam.read()
    writer.write(frame)
    cv.imshow("video", frame)
    if cv.waitKey(25) & 0xFF == ord("q"):
        break

cam.release()
writer.release()
cv.destroyAllWindows()