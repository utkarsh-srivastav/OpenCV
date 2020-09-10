import cv2

img = cv2.imread("C:\\Users\\hp\\Desktop\\DSC_6857.JPG")
print(img.shape)

imgResizeS = cv2.resize(img, (600, 300))
imgResizeL = cv2.resize(img, (900, 1800))

imgCrop = img[0:200, 200:500]

cv2.imshow("img", img)
cv2.imshow("Resized", imgResizeS)
cv2.imshow("Resized", imgResizeL)
cv2.imshow("Cropped", imgCrop)
cv2.waitKey(0)