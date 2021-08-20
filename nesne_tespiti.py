import cv2
import numpy as np

kamera=cv2.VideoCapture(0)

while True:
    ret,kare=kamera.read()
    gri_kare=cv2.cvtColor(kare,cv2.COLOR_BGR2GRAY)
    nesne=cv2.imread("tel.jpg",0)

    w,h=nesne.shape
    res=cv2.matchTemplate(gri_kare,nesne,cv2.TM_CCOEFF_NORMED)
    esik_degeri=0.8
    loc=np.where(res>esik_degeri)

    for n in zip(*loc[::-1]):
        cv2.rectangle(kare,n,(n[0]+h,n[1]+w),(0,255,0),2)
        cv2.putText(kare,"telefon",(n[0]+5,n[1]+5),cv2.FONT_HERSHEY_COMPLEX,1,[0,255,0],2)

    cv2.imshow("kare",kare)
    if cv2.waitKey(25) & 0xff == ord('q'):
        break

kamera.release()
cv2.destroyAllWindows()
