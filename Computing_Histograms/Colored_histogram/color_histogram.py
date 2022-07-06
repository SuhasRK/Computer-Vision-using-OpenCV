import cv2 as cv
from cv2 import resize

import matplotlib.pyplot as plt

img=cv.imread("/home/suhas/Desktop/Computer-Vision-using-OpenCV/Computing_Histograms/images/cat2.jpeg")
img=resize(img,(600,400))
cv.imshow('Image',img)

plt.figure()
plt.title("Color Histogram")

plt.xlabel("Bins")
plt.ylabel("No of pixels")

colors=['b','g','r']

for i,colors in enumerate(colors):
    hist=cv.calcHist([img],[i],None,[256],[0,256])
    plt.xlim([0,256])
    plt.plot(hist)
plt.show()
cv.waitKey(0)