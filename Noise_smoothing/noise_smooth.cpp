#include <opencv2/opencv.hpp>
#include <opencv2/highgui.hpp>
#include <iostream>
using namespace cv;
using namespace std;

int main(){

    string path="/home/suhas/Desktop/cpp_test/resources/noise.jpeg";
    Mat image=imread(path);

    Mat medianBlurImage,gaussianBlurImage;

    medianBlur(image,medianBlurImage,9);
    GaussianBlur(image,gaussianBlurImage,Size(5,5),9,9);

    imshow("Original Image",image);
    imshow("MedianBlur Image",medianBlurImage);
    imshow("GaussianBlur Image",gaussianBlurImage);
    waitKey(0);


}