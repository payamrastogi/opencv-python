import cv2
import numpy as np
print("Package Imported")

'''
image warp_perspective
'''
img = cv2.imread("resources/cards.jpg")
pts1 = np.float32([[111,219], [287,188], [154,482],[352,440]])
width, height = 250,350
pts2 = np.float32([[0,0],[width, 0],[0, height],[width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))
cv2.imshow("image", imgOutput)
cv2.waitKey(0)