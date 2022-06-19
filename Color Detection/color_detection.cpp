#include <stdio.h>
#include <opencv2/opencv.hpp>
using namespace cv;
using namespace std;

int hmin=90,smin=90,vmin=153;
int hmax=100,smax=110,vmax=255;

int main(){
    string path="C://Users//Lenovo//Downloads//blue_ball.jpg";
    Mat image=imread(path);
    
    Mat output1,output2;
    // Enter in BGR format
    // For RED
    inRange(image,Scalar(5,5,100),Scalar(40,40,255),output1);
    // For blue
    inRange(image,Scalar(217,130,0),Scalar(255,153,0),output2);

    int x1,x2;
    x1=countNonZero(output1);
    x2=countNonZero(output2);

    if (x1<x2){
        cout<< "Blue ball" << endl;
        imshow("output",output2);
    }

    else{
        cout<< "Red ball" << endl;
        imshow("output",output1);
    }


    imshow("Image",image);
    
    waitKey(0);
    
    


}