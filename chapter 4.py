import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
cv2.line(img, (170, 0), (img.shape[1], img.shape[0]), (0, 0, 255), 3)
cv2.rectangle(img, (0, 0), (150, 250), (0, 255, 0), 3)
cv2.circle(img, (400, 150), 80, (255, 0, 0), 5)
cv2.putText(img, " Hello Brother", (80, 350), cv2.FONT_ITALIC, 1, (255, 255, 0), 3)


cv2.imshow("Image", img)
cv2.waitKey(0)
