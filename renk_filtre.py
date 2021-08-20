import cv2
import numpy as np
kamera=cv2.VideoCapture(0)

dusuk=np.array([90,50,50])
yuksek=np.array([130,255,255])
while True:
    ret,goruntu=kamera.read()
    hsv=cv2.cvtColor(goruntu,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv,dusuk,yuksek)
    son_resim=cv2.bitwise_and(goruntu,goruntu,mask=mask)
    median=cv2.medianBlur(son_resim,15)
    bilateral=cv2.bilateralFilter(son_resim,15,75,75)
    cv2.imshow("bgr uzayında kamera",goruntu)
    cv2.imshow("hsv uzayında kamera",hsv)
    cv2.imshow("masklenmis",mask)
    cv2.imshow("son resim",son_resim)
    cv2.imshow("median",median)
    cv2.imshow("bilateral",bilateral)
    if cv2.waitKey(25) & 0xff == ord('q'):
        break

kamera.release()
cv2.destroyAllWindows()