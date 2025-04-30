import cv2
import numpy as np

image_path="gorsel\soccerframe.png"

kernel = np.ones((5,5),np.uint8)

image = cv2.imread(image_path)
image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
image_blur = cv2.GaussianBlur(image,(5,5),7)
image_Canny=cv2.Canny(image,100, 100)
image_Canny_Genis = cv2.dilate(image_Canny,kernel,4)
image_Canny_Dar = cv2.erode(image_Canny_Genis,kernel,4)

""" cv2.imshow("Normal",image)
cv2.imshow("Gri",image_gray)
cv2.imshow("Blur",image_blur) """   

cv2.imshow("Canny normal",image_Canny)
cv2.imshow("Canny genis",image_Canny_Genis)
cv2.imshow("Canny dar",image_Canny_Dar)

cv2.waitKey(0)
cv2.destroyWindow()