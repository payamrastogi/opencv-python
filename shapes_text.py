import cv2
import numpy as np
print("Package Imported")

'''
Draw blank/black image
'''
# img = np.zeros((512, 512))
# print (img)
# print (img.shape)
# cv2.imshow("output", img)
# cv2.waitKey(0)


'''
Draw color image
'''
# img = np.zeros((512, 512, 3), np.uint8)
# print (img.shape)
# img[:] = 255, 0, 0
# cv2.imshow("output", img)
# cv2.waitKey(0)


'''
color image section
'''
# img = np.zeros((512, 512, 3), np.uint8)
# print (img.shape)
# img[200:300, 100:300] = 255, 0, 0
# cv2.imshow("output", img)
# cv2.waitKey(0)

'''
line
'''
# img = np.zeros((512, 512, 3), np.uint8)
# cv2.line(img, (0, 0),(200, 100), (0, 255, 0), 3)## start and point, color , thickness
# cv2.imshow("output", img)
# cv2.waitKey(0)


'''
rectangle
'''
# img = np.zeros((512, 512, 3), np.uint8)
# cv2.rectangle(img, (0, 0),(250, 300), (0, 255, 0),2)## start and end point, color , thickness
# cv2.rectangle(img, (0, 0),(250, 300), (0, 255, 0),cv2.FILLED)## start and point, color , fill
# cv2.imshow("output", img)
# cv2.waitKey(0)

'''
circle
'''
# img = np.zeros((512, 512, 3), np.uint8)
# cv2.circle(img, (400, 100), 100,(255, 255, 0),5)## start and radius, color , fill
# cv2.imshow("output", img)
# cv2.waitKey(0)

'''
Text
'''
img = np.zeros((512, 512, 3), np.uint8)
cv2.putText(img, "OPENCV", (300, 100),cv2.FONT_HERSHEY_COMPLEX,1, (0, 150, 0), 1)## text, start, font ,,fontsize, color, thickness
cv2.imshow("output", img)
cv2.waitKey(0)