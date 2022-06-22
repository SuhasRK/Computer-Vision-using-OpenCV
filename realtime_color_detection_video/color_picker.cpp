#include <opencv2/opencv.hpp>
#include <opencv2/highgui.hpp>
#include <iostream>
using namespace cv;
using namespace std;

Mat imgHSV,mask,imgColor;

int hmin=0,smin=0,vmin=0;
int hmax=179,smax=255,vmax=255;

VideoCapture cap("http://192.168.0.102:8080/video");
Mat image;

int main(){
    namedWindow("Trackbars",(640,200));
    createTrackbar("Hue min","Trackbars",&hmin,179);
    createTrackbar("Hue max","Trackbars",&hmax,179);
    createTrackbar("Sat min","Trackbars",&smin,255);
    createTrackbar("Sat max","Trackbars",&smax,255);
    createTrackbar("Val min","Trackbars",&vmin,255);
    createTrackbar("Val max","Trackbars",&vmax,255);

    while(true){
        cap.read(image);
        resize(image,image,{600,400});
        cvtColor(image,imgHSV,COLOR_BGR2HSV);

        Scalar lower(hmin,smin,vmin);
        Scalar upper(hmax,smax,vmax);

        inRange(imgHSV,lower,upper,mask);

        cout << hmin << "," << hmax << "," << smin << "," << smax << "," << vmin << "," << vmax << endl;

        imshow("Image",image);
        imshow("Color detected",mask);

        waitKey(1);
    }

}