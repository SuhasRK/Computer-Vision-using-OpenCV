#include <stdio.h>
#include <opencv2/opencv.hpp>
#include <opencv2/objdetect.hpp>
using namespace cv;
using namespace std;


int main(){
    string path="D://imageProcessingCPP//opencv-cpp//Resources//face_pic.jpg";
    Mat image=imread(path);
    resize(image,image,Size(),0.25,0.25);

    CascadeClassifier faceCascade;
    faceCascade.load("D://imageProcessingCPP//opencv-cpp//Resources//harrcascade_frontalface_default.xml");

    if (faceCascade.empty()){
        cout<<"XML file not loaded"<<endl;
    }

    vector<Rect> faces;
    faceCascade.detectMultiScale(image,faces,1.1,10);

    for(int i=0;i<faces.size();i++){
        rectangle(image,Point(faces[i].tl()),Point(faces[i].br()),Scalar(0,255,0),2);
    }
    imshow("Image",image);
    waitKey(0);
}