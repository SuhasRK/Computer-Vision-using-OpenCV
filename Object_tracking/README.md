
# Object Tracking using OpenCV and python

For a given ROI(region of interest) in the first frame of the video, our code applies algorithms to trace that mentioned object in every upcoming frame of the video.


## Basically we use 8 models, which can be used independently to track the object.

So the models used are:

- BOOSTING
- MIL (multiple instance learning)
- KCF tracker (kernelized correlation filters)
- TLD tracker (Tracking,learning and detection)
- MEDIANFLOW tracker
- GOTURN tracker
- MOSSE tracker
- CSRT tracker (Correlation Filter with Channel and Spatial Reliability Tracking)


