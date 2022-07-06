import cv2 as cv
from cv2 import resize
import matplotlib.pyplot as plt
img=cv.imread("/home/suhas/Desktop/Computer-Vision-using-OpenCV/Computing_Histograms/images/cat2.jpeg")
img=resize(img,(600,400))
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Image",gray)

gray_hist=cv.calcHist([gray],[0],None,[256],[0,256])
plt.figure()
plt.title("Greyscale Histogram")

plt.xlabel("Bins")
plt.ylabel("No of pixels")

plt.xlim([0,256])
plt.plot(gray_hist)

plt.show()

cv.waitKey(0)