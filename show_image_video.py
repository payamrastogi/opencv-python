import cv2
print("Package Imported")

'''
image
'''
#img = cv2.imread("resources/lena.png")

#cv2.imshow("output", img)
#cv2.waitKey(0)


'''
video
'''

cap = cv2.VideoCapture(0)
cap.set(3, 640) #width
cap.set(4, 480) #height
cap.set(10, 60) #brightness
while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break