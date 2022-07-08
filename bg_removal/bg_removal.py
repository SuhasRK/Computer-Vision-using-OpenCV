from cgitb import reset
import cv2 as cv
from cv2 import resize
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os

from numpy import outer

cap=cv.imread("/home/suhas/Desktop/Computer-Vision-using-OpenCV/bg_removal/image.png")

segmentor=SelfiSegmentation()
output=segmentor.removeBG(cap,(255,255,255))

cap=resize(cap,(600,500))
output=resize(output,(600,500))
cv.imshow("Image",cap)
cv.imshow("Output",output)

cv.waitKey(0)