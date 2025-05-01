import cv2
import numpy as np

img = np.zeros((300,300,3),np.uint8)

img[:] = 20,100,255 #B-G-R

cv2.line(img,(0,100),(300,300),(0,0,255),5) # hangi görsel - ilk nokta (x,y) - ikinci nokta (x,y) - çizgi rengi - çizgi kalınlığı
#cv2.rectangle(img,(0,0),(300,100),(0,0,255),5)
cv2.rectangle(img,(0,0),(300,100),(0,0,255),cv2.FILLED) # İçini doldur
cv2.line(img,(300,100),(0,300),(0,0,255),5)
cv2.circle(img,(150,200),100,(0,0,255),5)
cv2.putText(img,"Decorous",(0,300),cv2.FONT_HERSHEY_SIMPLEX,2,(255,255,255),4) #hangi görsel - yazı - pozisyon - font - büyüklüğü - rengi - kalınlığı


cv2.imshow("resim",img)

cv2.waitKey(0)
cv2.destroyAllWindows()