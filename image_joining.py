import cv2
import numpy as np
print("Package Imported")

'''
image joining images
'''
##we cannot resize the image
## if images do not have same number of channels this method won't work
img = cv2.imread("resources/lena.png")

imgHor = np.hstack((img, img))
cv2.imshow("horizontal", imgHor)

imgVer = np.vstack((img, img))
cv2.imshow("vertical", imgVer)

cv2.waitKey(0)