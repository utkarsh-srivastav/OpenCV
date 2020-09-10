import cv2
import numpy as np

img = cv2.imread("C:\\Users\\hp\\Desktop\\imgc.jpg")

width, height = 300, 500
pts1 = np.float32([[571, 383], [997, 379], [267, 875], [1009, 899]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOp = cv2.warpPerspective(img, matrix, (width, height))


cv2.imshow("Image", img)
cv2.imshow("op", imgOp)

cv2.waitKey(0)

