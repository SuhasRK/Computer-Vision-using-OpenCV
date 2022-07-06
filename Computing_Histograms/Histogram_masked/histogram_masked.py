from cgitb import grey
import cv2 as cv
from cv2 import resize
from cv2 import circle
import matplotlib.pyplot as plt
import numpy as np
img=cv.imread("/home/suhas/Desktop/Computer-Vision-using-OpenCV/Computing_Histograms/images/cat2.jpeg")
img=resize(img,(600,400))

blank=np.zeros(img.shape[:2],dtype='uint8')

circle=cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow("Image",gray)

mask=cv.bitwise_and(gray,gray,mask=circle)
gray_hist=cv.calcHist([gray],[0],None,[256],[0,256])
cv.imshow("Image",mask)

plt.figure()
plt.title("Greyscale Histogram")

plt.xlabel("Bins")
plt.ylabel("No of pixels")

plt.xlim([0,256])
plt.plot(gray_hist)

plt.show()

cv.waitKey(0)