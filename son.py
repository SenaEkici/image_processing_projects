import cv2
import numpy as np


resim= cv2.imread("seinfeld.jpg")
cv2.imwrite("seinfeld_gri.jpg",resim)

cv2.imshow("Seinfeld" , resim)

cv2.waitKey(0)
cv2.destroyAllWindows()