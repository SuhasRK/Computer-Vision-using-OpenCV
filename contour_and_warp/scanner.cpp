#include <opencv2/opencv.hpp>
#include <opencv2/highgui.hpp>
#include <iostream>
using namespace cv;
using namespace std;

Mat image;
vector<Point> initialPoint;
vector<Point> docPoints;

Mat preProcessing(Mat input){
    
    Mat grey,blur,edges,dilated,eroded;

    cvtColor(input,grey,COLOR_BGR2GRAY);
    GaussianBlur(grey,blur,Size(3,3),3,0);
    Canny(blur,edges,25,75);

    Mat kernel=getStructuringElement(MORPH_RECT,Size(3,3));
    dilate(edges,dilated,kernel);
    // erode(dilated,eroded,kernel);

    return dilated;
}


vector<Point> getContours(Mat input)
{

    vector<vector<Point>> contours;
    vector<Vec4i> hierarchy;
    findContours(input,contours,hierarchy,RETR_EXTERNAL,CHAIN_APPROX_SIMPLE);
    vector<vector<Point>>conPoly(contours.size());

    vector<Point> biggest;

    int maxArea=0;
    for(int i=0;i<contours.size();i++){
        int area=contourArea(contours[i]);
        // cout<< area<<endl;
        

        if (area>=1000){
            float peri=arcLength(contours[i],true);
            approxPolyDP(contours[i],conPoly[i],0.02*peri,true);

            if (area>maxArea && conPoly[i].size()==4){
                biggest={conPoly[i][0],conPoly[i][1],conPoly[i][2],conPoly[i][3]};
                maxArea=area;
            }
            // cout<<conPoly[i].size()<<endl;
            drawContours(image,conPoly,i,Scalar(255,0,255),2);
            
            
        }
    }

    return biggest;
    
};

void drawPoints(vector<Point> points,Scalar color){
    for(int i=0;i<points.size();i++){
        circle(image,points[i],10,color,FILLED);
        putText(image,to_string(i),points[i],FONT_HERSHEY_COMPLEX,2,color,1);
    }
}

vector<Point> reorder(vector<Point> points){
    vector<Point> newPoint;
    vector<int> sumPoint,subPoint;

    for(int i=0;i<points.size();i++){
        sumPoint.push_back(points[i].x+points[i].y);
        subPoint.push_back(points[i].x-points[i].y);

    }

    newPoint.push_back(points[min_element(sumPoint.begin(),sumPoint.end())-sumPoint.begin()]);
    // newPoint.push_back(points[max_element(subPoint.begin(),subPoint.end())-subPoint.begin()]);
    // newPoint.push_back(points[min_element(subPoint.begin(),subPoint.end())-subPoint.begin()]);
    newPoint.push_back(points[3]);
    newPoint.push_back(points[1]);
    newPoint.push_back(points[max_element(sumPoint.begin(),sumPoint.end())-sumPoint.begin()]);

    return newPoint;
}

int main(){
    string path="/home/suhas/Desktop/cpp_test/resources/document.jpg";
    image=imread(path);
    Mat imgThre;
    resize(image,image,{600,400});

    //get thresholded image
    imgThre=preProcessing(image);
    // get contours initial point 
    initialPoint=getContours(imgThre);

    // for(int i;i<initialPoint.size();i++){
    //     cout<< initialPoint[i] <<endl;
    // }

    cout<<initialPoint<<endl;
    // cout<<"Hello"<<endl;
    
    // draw points 
    // drawPoints(initialPoint,Scalar(255,0,0));

    // reorder of points
    docPoints=reorder(initialPoint);

    cout<<docPoints<<endl;

    drawPoints(docPoints,Scalar(0,255,0));

    Mat matrix,warp_pers;
    float w=250,h=350;
    Point2f src[4]={docPoints[0],docPoints[1],docPoints[2],docPoints[3]};
    Point2f dst[4]={{0.0f,0.0f},{w,0.0f},{0.0f,h},{w,h}};

    matrix=getPerspectiveTransform(src,dst);
    warpPerspective(image,warp_pers,matrix,Point(w,h));


    imshow("Image",image);
    imshow("Image with Threshold",imgThre);
    imshow("Warp perspective",warp_pers);

    waitKey(0);
}