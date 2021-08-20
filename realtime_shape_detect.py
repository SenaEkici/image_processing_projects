import cv2
import numpy as np

kamera=cv2.VideoCapture(0)
dusuk=np.array([90,50,50])
yuksek=np.array([130,255,255])
while True:
    ret,goruntu=kamera.read()
    #hsv=cv2.cvtColor(goruntu,cv2.COLOR_BGR2HSV)
    gri=cv2.cvtColor(goruntu,cv2.COLOR_BGR2GRAY)
    #mavi=cv2.inRange(hsv,dusuk,yuksek)
    canny = cv2.Canny(gri, 100, 200)
    #kenar algılama
    contours,_=cv2.findContours(canny,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
     approx=cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
     area=cv2.contourArea(cnt)
     x=approx.ravel()[0]
     y=approx.ravel()[1]

     if area>400 :
       cv2.drawContours(goruntu, [approx], 0, [0, 255, 255], 5)
       print(len(approx))
       if len(approx)==4:
         cv2.putText(goruntu,"dortgen",(x,y),cv2.FONT_HERSHEY_PLAIN,2,[255,255,0],2)



    cv2.imshow("kamera",goruntu)
    #cv2.imshow("mavi",mavi)
    cv2.imshow("canny",canny)

    #cv2.imshow("mask",gri)
    key=cv2.waitKey(1)
    if key==25:
        break


kamera.release()
cv2.destroyAllWindows()