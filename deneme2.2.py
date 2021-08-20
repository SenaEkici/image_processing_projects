import cv2
import numpy as np


def  main():
 resim1=cv2.imread("concert.jpg")
 resim2=cv2.imread("elma2.jpg")

 res_gri=cv2.cvtColor(resim2,cv2.COLOR_BGR2GRAY)

 yukseklik,genislik,kanal = resim2.shape
 print(yukseklik,genislik,kanal)
 ROI=resim1[0:yukseklik,0:genislik]

 ret,mask=cv2.threshold(res_gri,10,255,cv2.THRESH_BINARY)
 mask_inverse = cv2.bitwise_not(mask)
 concert_arka=cv2.bitwise_and(ROI,ROI,mask=mask_inverse)

 toplam=cv2.add(concert_arka,resim2)
 resim1[0:yukseklik,0:genislik]=toplam
 cv2.imshow("sonuc",resim1)
 cv2.imshow("concert",resim1)
 cv2.imshow("resim2",resim2)
 cv2.imshow("gri_resim",res_gri)
 cv2.imshow("ters masklanmis resim",mask_inverse)
 cv2.imshow("masklanmis resim", mask)
 cv2.imshow("concert_arka",concert_arka)

 cv2.waitKey(0)
 cv2.destroyAllWindows()

if __name__ == "__main__":
     main()

