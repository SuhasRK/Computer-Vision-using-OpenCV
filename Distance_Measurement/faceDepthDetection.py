import cv2 as cv
import cvzone

from cvzone.FaceMeshModule import FaceMeshDetector

cap=cv.VideoCapture("http://192.168.0.102:8080/video")

detector = FaceMeshDetector(maxFaces=1)

while(True):
    success,frame=cap.read()
    frame=cv.resize(frame,(600,400))
    frame,faces=detector.findFaceMesh(frame,draw=True)

    if faces:
        faces=faces[0]
        pointLeft=faces[145]
        pointRight=faces[374]

        # Drawing part 

        cv.circle(frame,pointLeft,2,(255,0,255),cv.FILLED)
        cv.circle(frame,pointRight,2,(255,0,255),cv.FILLED)
        cv.line(frame,pointLeft,pointRight,(0,255,0),2)

        w,_=detector.findDistance(pointLeft,pointRight)

       
        # finding the focal length 
        W=6.3
        # d=50

        # f=(w*d)/W

        f=500
        d=(W*f)/w
        # print("distance:",d)
        cvzone.putTextRect(frame,f"Depth:{int(d)}cm",(faces[10][0]-75,faces[10][1]-50),scale=2)



    cv.imshow("Video",frame)

    if cv.waitKey(1) & 0xff==ord("q"):
        break


cv.destroyAllWindows()
