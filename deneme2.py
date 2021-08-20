import cv2

resim=cv2.imread("dororo.jpg")


#print(type(resim))

#print(resim.item(100,50,0))
#print(resim.item(100,50,1))
#print(resim.item(100,50,2))

#yuz=resim[0:300,150:500]

#print(resim.size)
#print(resim.dtype)
#print(resim.shape)


#resmi uzatma =>
#uzatilan_resim=cv2.copyMakeBorder(resim,100,100,100,100,cv2.BORDER_REPLICATE)

#resmi aydınlatma=>

#aynalama_resim=cv2.copyMakeBorder(resim,100,100,100,100,cv2.BORDER_REFLECT)

#resmi tekrarlama=>

#tekrarlanan_resim=cv2.copyMakeBorder(resim,100,100,100,100,cv2.BORDER_WRAP)

#resmin etrafını sarma=>

#sarilan_resim=cv2.copyMakeBorder(resim,100,100,100,100,cv2.BORDER_CONSTANT,value=[0,0,255])

#kare içine alma
cv2.rectangle(resim,(500,0),(150,300),[0,0,255],4)







cv2.imshow("dororo",resim)
#cv2.imshow("dororo uzama",uzatilan_resim)
#cv2.imshow("dororo tekrar",tekrarlanan_resim)
#cv2.imshow("dororo aynalama",aynalama_resim)
#cv2.imshow("dororo sarma",sarilan_resim)
#cv2.imshow("yuz",yuz)


cv2.waitKey()
cv2.destroyAllWindows()