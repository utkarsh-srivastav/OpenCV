import cv2
import numpy as np

def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area > 500:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 2)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.07*peri, True)
            print(len(approx))
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)

            if objCor == 3:
                objtype = "Tri"
            elif objCor == 4:
                aspratio = w/float(h)
                if aspratio > 0.95 and aspratio < 1.05:
                    objtype = "Square"
                else:
                    objtype = "Rectangle"
            else:
                objtype = "Circle"

            cv2.rectangle(imgContour, (x, y), (x+w, y+h), (255, 0, 0), 1)
            cv2.putText(imgContour, objtype, (x+(w//2)-10, y+(h//2)-10), cv2.FONT_ITALIC, 0.5, (0, 255, 255), 2)




img = cv2.imread("C:\\Users\\hp\\Desktop\\shapes2.png")
imgContour = img.copy()
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
imgCanny = cv2.Canny(imgBlur, 50, 50)
getContours(imgCanny)


cv2.imshow("Original", img)
cv2.imshow("Gray", imgGray)
cv2.imshow("Blur", imgBlur)
cv2.imshow("Canny", imgCanny)
cv2.imshow("cnt", imgContour)

cv2.waitKey(0)
