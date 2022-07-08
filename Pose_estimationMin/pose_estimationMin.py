import cv2 as cv
from cv2 import resize
from cv2 import COLOR_BGR2RGB
import mediapipe as mp
import time

mpPose=mp.solutions.pose
pose=mpPose.Pose()
mpDraw=mp.solutions.drawing_utils
cap=cv.VideoCapture('/home/suhas/Desktop/opencv-python/pose_estimationMin/videos/2.mp4')
pTime=0
while True:
    success,img=cap.read()
    img=resize(img,(800,550))
    imgRGB=cv.cvtColor(img,COLOR_BGR2RGB)
    results=pose.process(imgRGB)

    # print(results.pose_landmarks) 

    if results.pose_landmarks :
        mpDraw.draw_landmarks(img,results.pose_landmarks,mpPose.POSE_CONNECTIONS)
        h,w,c=img.shape
        for id,lm in enumerate(results.pose_landmarks.landmark):

            print(id,lm)
            cx,cy=int(lm.x*w),int(lm.y*h)
            cv.circle(img,(cx,cy),5,(255,0,0),cv.FILLED)
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    cv.putText(img,str(int(fps)),(70,50),cv.FONT_HERSHEY_COMPLEX,2,(255,0,0),3)
    cv.imshow('Video',img)
    
    cv.waitKey(10)
