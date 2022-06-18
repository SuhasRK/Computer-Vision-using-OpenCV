#include <stdio.h>
#include <opencv2/opencv.hpp>
using namespace cv;
using namespace std;

float w=250,h=350;

Mat matrix,warp_pers;

int main(){
    string path="C://Users//Lenovo//Downloads//cards_king.jpg";
    Mat image=imread(path);
    
    Point2f src[4]={{332,135},{581,150},{286,420},{593,441}};
    Point2f dst[4]={{0.0f,0.0f},{w,0.0f},{0.0f,h},{w,h}};

    matrix=getPerspectiveTransform(src,dst);
    warpPerspective(image,warp_pers,matrix,Point(w,h));

    for(int i=0;i<4;i++){
        circle(image,Point(src[i]),10,Scalar(0,0,255),FILLED);
    }
    imshow("warp_perspective",warp_pers);
    imshow("Original",image);
    waitKey(0);


}