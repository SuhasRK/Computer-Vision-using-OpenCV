import cv2 as cv
from cv2 import resize
from cv2 import INTER_AREA
import numpy as np

image = cv.imread('chair.jpg')

image=resize(image,(500,500),interpolation=INTER_AREA)

cv.imshow('Original Image', image)

grey = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

grey = np.float32(grey)

dest = cv.cornerHarris(grey, 2, 5, 0.07)

dest = cv.dilate(dest, None)

image[dest > 0.01 * dest.max()]=[0, 0, 255]


cv.imshow('Image after detecting edges', image)

if cv.waitKey(0) & 0xff == 27:
	cv.destroyAllWindows()
