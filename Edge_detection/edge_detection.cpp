#include <stdio.h>
#include <opencv2/opencv.hpp>
using namespace cv;
using namespace std;

int main(){
    Mat img = imread("D://imageProcessingCPP//opencv-cpp//Resources//face_pic.jpg");
    resize(img,img,Size(500,500));
    // Display original image
    imshow("original Image", img);
    // waitKey(0);

    Mat img_gray;
    cvtColor(img, img_gray, COLOR_BGR2GRAY);

    Mat img_blur;
    GaussianBlur(img_gray, img_blur, Size(3,3), 0);

    Mat sobelx, sobely, sobelxy;
    Sobel(img_blur, sobelx, CV_64F, 1, 0, 5);
    Sobel(img_blur, sobely, CV_64F, 0, 1, 5);
    Sobel(img_blur, sobelxy, CV_64F, 1, 1, 5);
    // Display Sobel edge detection images
    imwrite("D://imageProcessingCPP//opencv-cpp//Resources//sobelx.jpg",sobelx);
    imwrite("D://imageProcessingCPP//opencv-cpp//Resources//sobely.jpg",sobely);
    imwrite("D://imageProcessingCPP//opencv-cpp//Resources//sobelxy.jpg",sobelxy);

    destroyAllWindows();
    return 0;
}