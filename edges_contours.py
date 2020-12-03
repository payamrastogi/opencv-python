import cv2
import numpy as np
print("Package Imported")

'''
contours
'''
def getContours(img):
    contours,hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print (area)
        if area > 500:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            print(peri)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            print(len(approx)) # number of corners
            objCorner = len(approx)
            x,y,w,h = cv2.boundingRect(approx) ## bounding box
            
            if objCorner == 3:
                objectType = "Tri"
            elif objCorner == 4:
                aspectRatio = w/float(h)
                if aspectRatio > 0.95 and aspectRatio < 1.05:
                    objectType = "Square"
                else:
                    objectType  = "Rectangle"
            else:
                objectType = "None"
            cv2.rectangle(imgContour, (x,y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(imgContour, objectType,
                (x+(w//2)-10, y+(h//2)-10), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 0), 2)


'''
shape and color detection
'''
path = "resources/shapes.png"
img = cv2.imread(path)
imgContour = img.copy()
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)

imgCanny = cv2.Canny(imgBlur, 50, 50)
getContours(imgCanny)
cv2.imshow("output", img)
cv2.imshow("gray", imgGray)
cv2.imshow("blur", imgBlur)
cv2.imshow("canny", imgCanny)
cv2.imshow("canny", imgContour)
cv2.waitKey(0)