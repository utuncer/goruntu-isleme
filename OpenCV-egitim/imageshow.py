"""
import cv2

image_path = cv2.imread("gorsel/car.png",0)

h,w=image_path.shape[:2]

print("Yükseklik {}, Genişlik {}".format(h,w))

cv2.imwrite("gorsel/cikti/siyag-araba.png",image_path)
cv2.imshow("pencere",image_path)

cv2.waitKey(0)
"""

import cv2

image_path = "gorsel/car.png"
image_1 = cv2.imread(image_path)
image_2 = cv2.imread(image_path,0)

cv2.imwrite("gorsel/cikti/car1.jpg",image_1)
cv2.imwrite("gorsel/cikti/car2.jpg",image_2)