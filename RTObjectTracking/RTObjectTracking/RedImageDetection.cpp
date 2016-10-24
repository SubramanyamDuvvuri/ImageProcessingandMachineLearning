#include<opencv2\opencv.hpp>
#include<opencv2\highgui.hpp>
using namespace cv;

int main()
{
	Mat input;
	Mat imHSV;
	Mat output;
	VideoCapture camera(0);
	char charCheckForEscKey=0;
	if (camera.isOpened() == false) {				// check if VideoCapture object was associated to webcam successfully
		std::cout << "error: capWebcam not accessed successfully\n\n";	// if not, print error message to std out
		return(0);														// and exit program
	}

	while (charCheckForEscKey != 27 && camera.isOpened())
	{		// until the Esc key is pressed or webcam connection is lost
		bool blnFrameReadSuccessfully = camera.read(input);		// get next frame

		if (!blnFrameReadSuccessfully || input.empty()) {		// if frame not read successfully
			std::cout << "error: frame not read from webcam\n";		// print error message to std out
			break;													// and jump out of while loop
		}
		cvtColor(input, imHSV, CV_BGR2HSV);
		inRange(imHSV, cv::Scalar(10, 10, 80), cv::Scalar(60, 60, 255), output);
		//inRange(imgHSV, cv::Scalar(165, 155, 155), cv::Scalar(179, 255, 255), imgThreshHigh);

		namedWindow("image1", CV_WINDOW_FREERATIO);
		imshow("image1", output);

		namedWindow("image2", CV_WINDOW_FREERATIO);
		imshow("image2", input);
		waitKey(1);
	}
}
