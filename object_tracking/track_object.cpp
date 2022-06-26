#include <opencv2/opencv.hpp>
#include <opencv2/highgui.hpp>
#include <iostream>

#include<opencv2/tracking.hpp>
#include<opencv2/core/ocl.hpp>

using namespace cv;
using namespace std;

// Convert to string
#define SSTR( x ) static_cast< std::ostringstream & >( \
( std::ostringstream() << std::dec << x ) ).str()



int main(int argc,char **argv){
    string trackTypes[8] = {"BOOSTING","MIL","KCF","TLD","MEDIANFLOW", "GOTURN", "MOSSE", "CSRT"};

    string trackerType=trackTypes[2];

    Ptr<Tracker> tracker;

    if (CV_MINOR_VERSION<3){
        tracker = Tracker::create(trackerType);
    }


}
