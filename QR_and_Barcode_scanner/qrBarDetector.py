import cv2 as cv
from cv2 import VideoCapture
from cv2 import resize
import numpy as np

from pyzbar.pyzbar import decode 

# image=cv.imread("/home/suhas/Desktop/opencv-python/qrCode_detector/sample.png")
cap=VideoCapture("http://192.168.0.102:8080/video")

while(True):
    success,image=cap.read()

    image=resize(image,(800,600))
    for barcode in decode(image):
        print(barcode.rect)
        myData=barcode.data.decode('utf-8')
        print(myData)
        pts=np.array([barcode.polygon],np.int32)

        pts.reshape(-1,1,2)
        cv.polylines(image,[pts],True,(255,0,255),5)
        pts2=barcode.rect
        cv.putText(image,myData,(pts2[0],pts2[1]),cv.FONT_HERSHEY_COMPLEX,0.5,(0,255,0),2)

    cv.imshow("Result",image)

    if cv.waitKey(1) and 0xFF==ord('q'):
        break

cv.destroyAllWindows()



