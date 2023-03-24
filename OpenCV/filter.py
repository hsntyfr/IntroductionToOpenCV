import cv2 as cv

pic = cv.imread("pictures/train.jpg")
pic2 = cv.blur(pic, (3, 3)) # mean filtering
pic3 = cv.medianBlur(pic, 3) # median filtering
pic4 = cv.GaussianBlur(pic, (5, 5), 0) # gauss filter


cv.imshow("original", pic)
cv.imshow("mean filter", pic2)
cv.imshow("median filter", pic3)
cv.imshow("gauss filter", pic4)





cv.waitKey(0)
cv.destroyAllWindows()