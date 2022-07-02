import cv2
import numpy as np

image = cv2.imread('blob_input.png', 0)

params = cv2.SimpleBlobDetector_Params()

params.filterByArea = True
params.minArea = 100

detector = cv2.SimpleBlobDetector_create(params)
keypoints = detector.detect(image)

blank = np.zeros((1, 1))
blobs = cv2.drawKeypoints(image, keypoints, blank, (0, 0, 255),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imwrite("/home/suhas/Desktop/opencv-python/blob_detection/blob_output.png", blobs)
cv2.waitKey(0)
cv2.destroyAllWindows()