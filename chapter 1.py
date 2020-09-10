import cv2
'''
# code for reading image
img = cv2.imread("path of the img")
cv2.imshow("Output", img)
cv2.waitKey(0)
'''

'''
# code for reading a video
cap = cv2.VideoCapture("C:\\Users\\hp\\Desktop\\VID_20200909_140427.mp4")
while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
'''

# code for accessing the webCam
cap = cv2.VideoCapture(0)

# setting window size
cap.set(3,640)
cap.set(4,480)

# setting brightness
cap.set(10, 100)
while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
