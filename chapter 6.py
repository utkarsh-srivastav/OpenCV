import cv2
import numpy as np
img = cv2.imread("C:\\Users\\hp\\Desktop\\DSC_6847.JPG")

imgHor = np.hstack((img, img))
imgResizeH = cv2.resize(imgHor, (600, 300))
imgVer = np.vstack((img, img))
imgResizeV = cv2.resize(imgVer, (600, 300))

cv2.imshow("Image", img)
cv2.imshow("op1", imgResizeH)
cv2.imshow("op2", imgResizeV)

cv2.waitKey(0)
