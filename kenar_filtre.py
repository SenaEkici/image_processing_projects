import cv2
import numpy as np

kamera=cv2.VideoCapture(0)

while True:
    ret,goruntu=kamera.read()
    canny=cv2.Canny(goruntu,100,200)

    cv2.imshow("kamera",goruntu)
    cv2.imshow("canny",canny)

    if cv2.waitKey(25) & 0xff ==ord('q'):
        break


kamera.release()
cv2.destroyAllWindow()