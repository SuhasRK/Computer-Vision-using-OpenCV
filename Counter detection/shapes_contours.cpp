#include <stdio.h>
#include <opencv2/opencv.hpp>
using namespace cv;
using namespace std;

void getContours(Mat input,Mat output)
{
    vector<vector<Point>> contours;
    vector<Vec4i> hierarchy;
    findContours(input,contours,hierarchy,RETR_EXTERNAL,CHAIN_APPROX_SIMPLE);
    vector<vector<Point>>conPoly(contours.size());
    vector<Rect> boundRect(contours.size());
    string objectType;
    for(int i=0;i<contours.size();i++){
        int area=contourArea(contours[i]);
        cout<< area<<endl;
        

        if (area>=1000){
            float peri=arcLength(contours[i],true);
            approxPolyDP(contours[i],conPoly[i],0.02*peri,true);
            cout<<conPoly[i].size()<<endl;
            drawContours(output,conPoly,i,Scalar(255,0,255),2);
            boundRect[i]=boundingRect(conPoly[i]);
            rectangle(output,boundRect[i].tl(),boundRect[i].br(),Scalar(0,255,0),2);
            
            int objCol=(int)conPoly[i].size();

            if (objCol==3){
                objectType="Triangle";
            }
            else if(objCol==4){
                objectType="Square";
            }
            else if(objCol==5){
                objectType="Pentagon";
            }
            else if(objCol==6){
                objectType="Hexagon";
            }

            else{
                objectType="Unknown";
            }

            putText(output,objectType,{boundRect[i].x+5,boundRect[i].y+boundRect[i].height+10},FONT_HERSHEY_COMPLEX,0.5,Scalar(0,0,255),2);
            
        }
    }
    
};



int main(){
    
    
    Mat blur;
    string path="C://Users//Lenovo//Downloads//shapes.png";
    Mat grey,edges,dilated;
    Mat image=imread(path);
    // PREPROCESSING
    cvtColor(image,grey,COLOR_BGR2GRAY);
    GaussianBlur(grey,blur,Size(3,3),3,0);
    Canny(blur,edges,25,75);

    Mat kernel=getStructuringElement(MORPH_RECT,Size(3,3));
    dilate(edges,dilated,kernel);

    getContours(dilated,image);
    imshow("Image",image);
    waitKey(0);
}