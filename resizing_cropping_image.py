import cv2
import numpy as np
print("Package Imported")

'''
image size
'''
# img = cv2.imread("resources/lambo.png")
# print (img.shape)
# cv2.imshow("Image", img)
# cv2.waitKey(0)

'''
image resize
'''
# img = cv2.imread("resources/lambo.png")
# print (img.shape)
# #imgResize = cv2.resize(img, (300, 200))
# imgResize = cv2.resize(img, (1000, 500))
# cv2.imshow("Image", img)
# cv2.imshow("imgResize", imgResize)
# print (imgResize.shape)
# cv2.waitKey(0)


'''
image cropping
'''
img = cv2.imread("resources/lambo.png")
print (img.shape)

##height followed by width
imgCropped = img[0:200, 300:500]
cv2.imshow("Image", img)
cv2.imshow("Cropped Image", imgCropped)
cv2.waitKey(0)