import cv2 as cv
import sys 
import time

from cv2 import VideoCapture
from cv2 import boundingRect
from cv2 import resize

(major_ver, minor_ver, subminor_ver) = (cv.__version__).split('.')

tracker_types = ['BOOSTING', 'MIL','KCF', 'TLD', 'MEDIANFLOW', 'GOTURN', 'MOSSE', 'CSRT']

tracker_type= tracker_types[1]

if int(minor_ver)<3:
    tracker = cv.Tracker_create(tracker_type)

else:
    if tracker_type == 'BOOSTING':
            tracker = cv.TrackerBoosting_create()

    if tracker_type == 'MIL':
            tracker = cv.TrackerMIL_create()

    if tracker_type == 'KCF':
            tracker = cv.TrackerKCF_create()

    if tracker_type == 'TLD':
            tracker = cv.TrackerTLD_create()
    
    if tracker_type == 'MEDIANFLOW':
            tracker = cv.TrackerMedianFlow_create()

    if tracker_type == 'GOTURN':
            tracker = cv.TrackerGOTURN_create()

    if tracker_type == 'MOSSE':
            tracker = cv.TrackerMOSSE_create()

    if tracker_type == 'CSRT':
            tracker = cv.TrackerCSRT_create()


    cap=cv.VideoCapture("/home/suhas/Desktop/opencv-python/Object_track/sample2_edited.mp4")
    
    

    if not cap.isOpened():
        print("Could not open camera")
        sys.exit()

    success,frame=cap.read()

    if not success:
        print("Could not read content")
        sys.exit()

    # initial co-o
    # bbox=(287,23,86,320)

    bbox=cv.selectROI(frame,False)

    success = tracker.init(frame,bbox)

    while True:
        ok,frame=cap.read()
        # frame=resize(cap,(600,400))
        

        if not ok:
                break

        timer=cv.getTickCount()

        # update the frame 
        ok,bbox=tracker.update(frame)

        fps=cv.getTickFrequency() / (cv.getTickCount() - timer)

        if ok:
                # tracking is successful 
                p1=(int(bbox[0]),int(bbox[1]))
                p2=(int(bbox[0]+bbox[2]),int(bbox[1]+bbox[3]))

                cv.rectangle(frame,p1,p2,(255,0,0),2,1)

        else:
                # tracking failed 
                cv.putText(frame,"Failure to track",(100,80),cv.FONT_HERSHEY_COMPLEX,0.75,(50,170,50),2)

        # Display tracker type 
        cv.putText(frame,tracker_type+" Tracker",(100,20),cv.FONT_HERSHEY_COMPLEX,0.75,(50,170,50),2)

        # Display fps 
        cv.putText(frame,"FPS: "+str(int(fps)),(100,50),cv.FONT_HERSHEY_COMPLEX,0.75,(50,170,50),2)

        cv.imshow("Tracking image",frame)

        if cv.waitKey(1) & 0xff==ord("q"):
                break

cv.destroyAllWindows()
