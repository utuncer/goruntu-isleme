import cv2
import numpy as np

image1_path="gorsel\soccerframe.png"
image2_path="gorsel\car.png"

img1=cv2.imread(image1_path)
img2=cv2.imread(image2_path)

img1=cv2.resize(img1,(640,360))
img2=cv2.resize(img2,(640,360))

img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img1 = cv2.cvtColor(img1, cv2.COLOR_GRAY2BGR)

dikeybirlestir=np.hstack((img1,img2))
yataybirlestir=np.vstack((img1,img2))

cv2.imshow("dikey",dikeybirlestir)
cv2.imshow("yatay",yataybirlestir)

""" img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img1_bgr = cv2.cvtColor(img1_gray, cv2.COLOR_GRAY2BGR) """

cv2.waitKey(0)
cv2.destroyAllWindows()