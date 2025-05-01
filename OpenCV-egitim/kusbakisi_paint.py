import cv2
import numpy as np

img = cv2.imread("gorsel/tahta.jpg")

# (129, 259), (321, 239), (171,477), (366, 461) Görsel'in belirlediğimiz noktaları
# circle metodu int değeri alması gerektiğinden çevirmek zorunda kaldık

genislik, yukseklik = 640, 360

points = np.float32([[129,259],[321,239],[171,477],[366,461]])
canvas = np.float32([[0,0],[genislik,0],[0,yukseklik],[genislik,yukseklik]])
matrix = cv2.getPerspectiveTransform(points,canvas)
sonuc=cv2.warpPerspective(img,matrix,(genislik,yukseklik))

for i in range (len(points)):
    cv2.circle(img,((int(points[i][0])),(int(points[i][1]))),5,(0,0,255),cv2.FILLED)

cv2.imshow("gorsel",img)
cv2.imshow("kus bakisi",sonuc)


cv2.waitKey(0)
cv2.destroyAllWindows()
