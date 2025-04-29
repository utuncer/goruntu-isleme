import cv2

image_path = "gorsel\soccerframe.png"

img = cv2.imread(image_path)
#open cvde renk kodu krımızı - yeşil - mavi şeklinde değil! maviye - yeşil - kırmızı şeklinde sıralanır
#BGR olarak alır
cv2.imshow("futbol sahasi", img)

# grafikte x=1 y=1 olan kısmındaki pixelin renk kodunu alıyoruz
mavi = img.item(1,1,0)
yesil = img.item(1,1,1)
kirmizi = img.item(1,1,2)

print("{}, {}, {}".format(kirmizi,yesil,mavi))




cv2.waitKey(0)

