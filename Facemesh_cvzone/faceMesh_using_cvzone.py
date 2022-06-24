import cv2 as cv
import cvzone

from cvzone.FaceMeshModule import FaceMeshDetector

cap=cv.VideoCapture("http://192.168.0.102:8080/video")

detector = FaceMeshDetector(maxFaces=1)

while(True):
    success,frame=cap.read()
    frame=cv.resize(frame,(600,400))
    frame,faces=detector.findFaceMesh(frame)

    cv.imshow("Video",frame)

    if cv.waitKey(1) & 0xff==ord("q"):
        break


cv.destroyAllWindows()
