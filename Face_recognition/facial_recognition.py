from base64 import encode
from unittest import result
import cv2 as cv
from cv2 import resize
import numpy as np
import face_recognition

elonImg=face_recognition.load_image_file("elon_musk.jpg")
elonImg=resize(elonImg,(600,600))
ImgTest=face_recognition.load_image_file("bill_gates.jpg")
ImgTest=resize(ImgTest,(600,600))

elonImg=cv.cvtColor(elonImg,cv.COLOR_BGR2RGB)
ImgTest=cv.cvtColor(ImgTest,cv.COLOR_BGR2RGB)

faceLoc=face_recognition.face_locations(elonImg)[0]
faceLocTest=face_recognition.face_locations(ImgTest)[0]

encodeElon=face_recognition.face_encodings(elonImg)[0]

encodeTest=face_recognition.face_encodings(ImgTest)[0]
# print(encodeElon)

cv.rectangle(elonImg,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,255),2)
cv.rectangle(ImgTest,(faceLocTest[3],faceLocTest[0]),(faceLocTest[1],faceLocTest[2]),(255,0,255),2)


results=face_recognition.compare_faces([encodeElon],encodeTest)
faceDis=face_recognition.face_distance([encodeElon],encodeTest)
print(results,faceDis)

if faceDis[0]>0.5:
    cv.putText(ImgTest,"Face did not match",(ImgTest.shape[1]//2-50,ImgTest.shape[0]-10),cv.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
else:
    cv.putText(ImgTest,"Face matched",((ImgTest.shape[1]//2-50,ImgTest.shape[0]-10)),cv.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)

cv.putText(ImgTest,f'{results} {round(faceDis[0],2)}',(50,50),cv.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
cv.imshow("Image",elonImg)
cv.imshow("Test image",ImgTest)

cv.waitKey(0)