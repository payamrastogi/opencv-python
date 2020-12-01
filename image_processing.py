import cv2
import numpy as np
print("Package Imported")

'''
color to gray image
'''
# img = cv2.imread("resources/lena.png")
# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Gray Image", imgGray)
# cv2.waitKey(0)

'''
blur image
'''
# img = cv2.imread("resources/lena.png")
# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
# cv2.imshow("Gray Image", imgGray)
# cv2.imshow("Blur Image", imgBlur)
# cv2.waitKey(0)

'''
edge detector using Canny
'''
# img = cv2.imread("resources/lena.png")
# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
# #imgCanny = cv2.Canny(img,100, 100)
# imgCanny = cv2.Canny(img,150, 200)
# cv2.imshow("Gray Image", imgGray)
# cv2.imshow("Blur Image", imgBlur)
# cv2.imshow("Canny Image", imgCanny)
# cv2.waitKey(0)


'''
dilation
'''
# kernel = np.ones((5,5), np.uint8)
# img = cv2.imread("resources/lena.png")
# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
# #imgCanny = cv2.Canny(img,100, 100)
# imgCanny = cv2.Canny(img,150, 200)
# imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
# #cv2.imshow("Gray Image", imgGray)
# #cv2.imshow("Blur Image", imgBlur)
# cv2.imshow("Canny Image", imgCanny)
# cv2.imshow("Dialation Image", imgDialation)
# cv2.waitKey(0)


'''
erosion
'''
kernel = np.ones((5,5), np.uint8)
img = cv2.imread("resources/lena.png")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
#imgCanny = cv2.Canny(img,100, 100)
imgCanny = cv2.Canny(img,150, 200)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)
#cv2.imshow("Gray Image", imgGray)
#cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dialation Image", imgDialation)
cv2.imshow("Eroded Image", imgEroded)
cv2.waitKey(0)