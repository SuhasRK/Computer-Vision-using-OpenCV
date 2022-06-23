import cv2 as cv
from cv2 import imread
from cv2 import resize

import mediapipe as mp

# load facemesh
mp_face_mesh=mp.solutions.face_mesh
face_mesh=mp_face_mesh.FaceMesh()


# Image 
image=imread("/home/suhas/Desktop/opencv-python/Facemesh_detetcion/person1.jpeg")
image=resize(image,(650,500))
image2=imread("/home/suhas/Desktop/opencv-python/Facemesh_detetcion/person1.jpeg")
image2=resize(image2,(650,500))

imageRGB=cv.cvtColor(image,cv.COLOR_BGR2RGB)

# facial landmarks
result=face_mesh.process(imageRGB)

for facial_landmarks in result.multi_face_landmarks:
    # print(facial_landmarks)
    for id,lm in enumerate(facial_landmarks.landmark):
        # print(id,lm)
        h,w,c=image.shape
        cx,cy=int(lm.x*w),int(lm.y*h)

        # print(id,cx,cy)
        cv.circle(image2,(cx,cy),2,(0,255,0),cv.FILLED)

cv.imshow("Image",image)
cv.imshow("Output",image2)

cv.waitKey(0)