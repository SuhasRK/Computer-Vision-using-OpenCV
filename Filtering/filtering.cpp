#include <opencv2/opencv.hpp>
#include <iostream>
using namespace std;
using namespace cv;

int main()
{
    // Read Image
    Mat image = imread("D://imageProcessingCPP//opencv-cpp//Resources//example.jpg");

    // Print Error message if image is null
    if (image.empty()) 
        {
            cout << "Could not read image" << endl;
        }
    
    // Apply identity filter using kernel
    Mat kernel1 = (Mat_<double>(3,3) << 0, 0, 0, 0, 1, 0, 0, 0, 0);
    Mat identity; 
    filter2D(image, identity, -1 , kernel1, Point(-1, -1), 0, 4);
    imshow("Original", image);
    imshow("Identity", identity);
    waitKey();
    imwrite("identity.jpg", identity);
    destroyAllWindows();

    // Blurred using kernel
    // Initialize matrix with all ones
    Mat kernel2 = Mat::ones(5,5, CV_64F);
    // Normalize the elements
    kernel2 = kernel2 / 25;
    Mat img;
    filter2D(image, img, -1 , kernel2, Point(-1, -1), 0, 4);
    imshow("Original", image);
    imshow("Kernel blur", img);
    imwrite("D://imageProcessingCPP//opencv-cpp//Resources//output_img.jpg", img);
    waitKey(0);
    destroyAllWindows();
}