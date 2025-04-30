import cv2

image_path ="gorsel\soccerframe.png"

image = cv2.imread(image_path)
yukseklik, genislik = int(image.shape[0]/3),int(image.shape[1]/3)
imageRes= cv2.resize(image,(genislik,yukseklik)) # image.shape[0] değeri yüksekliği, image.shape[1] değeri genişliği, image.shape[2] renk kanalı sayısını gösterir. cv2.resize komutunu kullanırken ilk önce genişlik sonra yükseklik değeri girmemiz gerekir.
imageCrop = imageRes[:, 230:genislik-280] # crop


#cv2.imshow("normal",image)
cv2.imshow("kucuk",imageRes)
cv2.imshow("kucuk kirpilmis",imageCrop)

cv2.waitKey(0)
cv2.destroyAllWindows()