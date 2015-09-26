#include "opencv2/objdetect/objdetect.hpp"
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/imgproc/imgproc.hpp"
#include <opencv2/opencv.hpp>

#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
/*
 * Test trained cascade classifier
 * 
 */ 

using namespace std;
using namespace cv;

void detectAndDisplay( Mat frame )
{

    std::vector<Rect> faces;
    Mat frame_gray;

    cvtColor( frame, frame_gray, CV_BGR2GRAY );
    equalizeHist( frame_gray, frame_gray );

    //-- Detect faces
//    CascadeClassifier testCascade("cascadehog/cascade.xml");
   // HOGDescriptor testCascade("cascadehog/cascade.xml");
	HOGDescriptor testCascade;
//	testCascade.setSVMDetector(cv::HOGDescriptor::getDefaultPeopleDetector());
	assert (testCascade.load("cascadehog/cascade.xml"));
   // testCascade.detectMultiScale( frame_gray, faces, 1.1, 3, 0, Size(40, 40), Size(130, 130) );
 //   testCascade.detectMultiScale( frame_gray, faces,foundWeights,  0, Size(8, 8), Size(32, 32),1.05,2,false );
 //	std::cout << testCascade.blockStride << std::endl;
// 	std::cout << testCascade.getDescriptorSize() << std::endl;
	cin.get();
    testCascade.detectMultiScale( frame_gray, faces);
    std::cout << faces.size() << " Objects found " << std::endl;

    for( size_t i = 0; i < faces.size(); i++ )
    {
        //Point center( faces[i].x + faces[i].width*0.5, faces[i].y + faces[i].height*0.5 );
        cv::rectangle(
                frame,
                cv::Point(faces[i].x, faces[i].y),
                cv::Point(faces[i].x + faces[i].width, faces[i].y + faces[i].height),
                cv::Scalar(0, 0, 255),
                2
                );

    }

    //-- Show what you got
    // resize(frame, frame, cv::Size(512,512));
    imshow( "feh", frame );
    cv::waitKey(0);
}

std::string custom_to_string( const int n ){
    std::ostringstream stm ;
    stm << n ;
    return stm.str() ;
}


int main( int argc, const char** argv )
{

    for(int i = 0; i < 39; i++){
 //       std::string img_location = "data/testimages_size/w_" + custom_to_string(i) + ".jpg"; 
        std::string img_location = "data/testimages_size/people.jpg"; 
        Mat img = imread( (char*)img_location.c_str(), 1 );//, cv::IMREAD_COLOR
        detectAndDisplay(img); }
    printf("SUCCESS!\n");
    return 0;
}

