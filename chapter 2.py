import cv2
import numpy as np

img = cv2.imread("C:\\Users\\hp\\Desktop\\DSC_6857.JPG")
kernal = np.ones((5, 5), np.uint8)  # 5*5 matrix of ones, values can be changed to any unsigned int of 8 bits

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # converting img to gray scale
imgBlur = cv2.GaussianBlur(img, (7, 7), 0)  # converting img to Blur
imgCanny = cv2.Canny(imgGray, 200, 350) # converting img to sketch with edges only
imgDilation = cv2.dilate(imgCanny, kernal, iterations=1) # edge thickness depends on iteration value
imgErosion = cv2.erode(imgDilation, kernal, iterations=1)   # opposite of dilation

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dilate Image", imgDilation)
cv2.imshow("Erode Image", imgErosion)
cv2.waitKey(0)