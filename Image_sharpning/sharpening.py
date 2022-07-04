from cgitb import reset
import cv2 as cv
from cv2 import GaussianBlur
from cv2 import resize

import numpy as np

img = cv.imread("/home/suhas/Desktop/opencv-python/Image_sharpning/less_sharp.jpg")
img=resize(img,(500,400))

# gaussian blurring 
gaussian_blur=cv.GaussianBlur(img,(7,7),2)

# sharpning the images 
sharpened1=cv.addWeighted(img,1.5,gaussian_blur,-0.5,0)
sharpened2=cv.addWeighted(img,3.5,gaussian_blur,-2.5,0)
sharpened3=cv.addWeighted(img,7.5,gaussian_blur,-6.5,0)

cv.imshow("input",img)

cv.imwrite("/home/suhas/Desktop/opencv-python/Image_sharpning/sharpened1.jpg",sharpened1)
cv.imwrite("/home/suhas/Desktop/opencv-python/Image_sharpning/sharpened2.jpg",sharpened2)
cv.imwrite("/home/suhas/Desktop/opencv-python/Image_sharpning/sharpened3.jpg",sharpened3)

cv.waitKey(0)
