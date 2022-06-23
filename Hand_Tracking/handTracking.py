from unittest import result
import cv2 as cv
from cv2 import imshow
from cv2 import waitKey
from cv2 import resize
from cv2 import cvtColor
from cv2 import FONT_HERSHEY_COMPLEX
from matplotlib.pyplot import draw
import mediapipe as mp
import time


cap=cv.VideoCapture("http://192.168.0.102:8080/video")

mphands=mp.solutions.hands
hands=mphands.Hands()
mpDraw=mp.solutions.drawing_utils

pTime=0
cTime=0

while(True):
    success,image=cap.read()
    image=resize(image,(600,400))
    imgRGB=cv.cvtColor(image,cv.COLOR_BGR2RGB)
    results=hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id,lm in enumerate(handLms.landmark):
                # print(id,lm)
                h,w,c=image.shape
                cx,cy=int(lm.x*w),int(lm.y*h)

                print(id,cx,cy)

                if id==0:
                    cv.circle(image,(cx,cy),10,(255,0,255),cv.FILLED)
            mpDraw.draw_landmarks(image,handLms,mphands.HAND_CONNECTIONS)

    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime

    cv.putText(image,str(int(fps)),(10,70),cv.FONT_HERSHEY_COMPLEX,2,(255,0,255),3)


    cv.imshow("Image",image)
    
    if cv.waitKey(1) & 0xff == ord("q"):
        cv.destroyAllWindows()
        break

