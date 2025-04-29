import cv2

fraWeidth=640
frameHeight=360

#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture("video/soccer.mp4")

while True:
    # x başarı durumudur boolean değeridir.
    x,img = cap.read()
    img = cv2.resize(img,(fraWeidth,frameHeight))
    cv2.imshow("video1",img)

    if cv2.waitKey(25) & 0XFF == ord("q"): #waitKey'den dönen sayı ile 0xFF arasında & işlemi yapıldığında, sonuç olarak sadece sayının son 8 biti (yani 0-255 aralığına denk gelen kısmı) kalır.
        break   
    
cap.release()
cv2.destroyAllWindows()