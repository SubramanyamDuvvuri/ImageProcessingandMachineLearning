/*C++ code to track the object and to count the number of fingers
Steps to follow
1.Convert the Image to HSV
2.Draw contours
3.Draw convex hull
4.Find convexity defects
5. Count the fingers
*/
//Adding opencv libraries
#include<iostream>
#include<opencv2\opencv.hpp>
#include<opencv2\highgui\highgui.hpp>
#include<opencv2/core/core.hpp>
#include<opencv\cv.h>
using namespace cv;
using namespace std;
//Function declarations
void addBars(); //For taskBars
void doMorph(Mat&);// for adding erode and dillute
void onTrackBar(int, void*);
void showimgcontours(Mat &hsv_temp, Mat &original); // displaying contours
void finddefects(vector<Vec4i>, vector<Point>, Mat &);// displaying defects
int hmin = 65, hmax = 149, vmin = 8, vmax = 67, smin = 0, smax = 85, E = 3, D = 4; // initzing HSV values
int Echange = 1, Dchange = 1;
Mat erodeElement;
Mat dilateElement;
int main()
{
	Mat input;
	Mat hsv;
	Mat gray;
	onTrackBar(0, 0);
	bool morph = false;
	vector<Vec4i> hierarchy;
	//find contours of filtered image using openCV findContours function
	vector< vector<Point> > contours;
	vector<Vec3f> v3fCircles;
	//erodeElement = getStructuringElement(MORPH_RECT, Size(3,3));
	//dilateElement = getStructuringElement(MORPH_RECT, Size(3, 3));
	//erode(hsv, hsv, erodeElement);
	//dilate(hsv, hsv, dilateElement);
	VideoCapture camera(0); //Use 0 for default camera
	camera.set(CV_CAP_PROP_BUFFERSIZE, 0);
	// image can be flipped using flip function
	while (camera.isOpened())
	{
		bool getimage = camera.read(input); //geiing the image to the matrix
		if (!getimage || input.empty())
		{
			cout << "Image is inaccissable";
			break;
		}
		flip(input, input, 180);
		addBars();
		//convert from BGR to HSV
		cvtColor(input, hsv, CV_BGR2HSV);
		//cvtColor(gray, hsv, CV_BGR2HSV);
		//converting image to HSV through inrange function
		inRange(input, Scalar(hmin, smin, vmin), Scalar(hmax, smax, vmax), hsv);
		doMorph(hsv);
		imshow("HSV", hsv); //Displaying HSV image
		
		Mat hsv_temp;
		inRange(input, Scalar(hmin, smin, vmin), Scalar(hmax, smax, vmax), hsv_temp);
		//namedWindow("Window", CV_WINDOW_AUTOSIZE);
		showimgcontours(hsv_temp, input);
		imshow("window1", input);
		//imshow("HSV2", hsv);
		waitKey(1);
	}
	return 0;
}
//Creating Task bars to adjust the values
void addBars()
{
	namedWindow("Track Bars", CV_WINDOW_FREERATIO);
	createTrackbar("H_Min", "Track Bars", &hmin, 255, onTrackBar);
	createTrackbar("H_Max", "Track Bars", &hmax, 255, onTrackBar);
	createTrackbar("S_MIN", "Track Bars", &smin, 255, onTrackBar);
	createTrackbar("S Max", "Track Bars", &smax, 255, onTrackBar);
	createTrackbar("V MIN", "Track Bars", &vmin, 255, onTrackBar);
	createTrackbar("V Max", "Track Bars", &vmax, 255, onTrackBar);
	createTrackbar("Erode", "Track Bars", &E, 31, onTrackBar);
	createTrackbar("Dillate", "Track Bars", &D, 31, onTrackBar);
}
//For erode and dillate
void doMorph(Mat &hsv)
{
	erode(hsv, hsv, getStructuringElement(MORPH_RECT, Size(E, E)));
	dilate(hsv, hsv, getStructuringElement(MORPH_RECT, Size(D, D)));
	return;
}
void onTrackBar(int, void*)
{
	if (E == 0)
		E = 1;
	if (D == 0)
		D = 1;
}
//Function to display contours
void showimgcontours(Mat &hsv_temp, Mat &input)
{
	Mat temp(hsv_temp);
	vector<vector<Point>> contours;
	vector<Vec4i> hierarchy;
	int largest_area = 0;
	int largest_contour_index = 0;
	findContours(temp, contours, hierarchy, CV_RETR_TREE, CV_CHAIN_APPROX_SIMPLE);
	vector<vector<Vec4i> >defectsPoints(contours.size());
	vector<vector<int> >hull_int(contours.size());
	vector<vector<Point>>hull(contours.size());
	//Finding largest contour
	for (int i = 0; i < contours.size(); i++)
	{
		convexHull(contours[i], hull[i], false);
		convexHull(Mat(contours[i]), hull_int[i], false);
		if (hull_int[i].size()>3)
			convexityDefects(contours[i], hull_int[i], defectsPoints[i]); //finding defects
	}
	for (int i = 0; i< contours.size(); i++)
	{
		double a = contourArea(contours[i], false); // Finding contour area
		if (a>largest_area)
		{
			largest_area = a;
			largest_contour_index = i; //Storing largest contour index
		}
	}
	if (contours.size() > 0)
	{
		drawContours(input, contours, largest_contour_index, CV_RGB(0, 255, 0), 2, 8, hierarchy);
		//To display all contours
		//drawContours(input,contours,-1, CV_RGB(100, 255, 100), 2, 8, hierarchy);
		drawContours(input, hull, largest_contour_index, CV_RGB(0, 0, 255), 2, 8, hierarchy);
		finddefects(defectsPoints[largest_contour_index], contours[largest_contour_index], input);
	}
}
void finddefects(vector<Vec4i> defectsPoints, vector<Point> mycontour, Mat &input)
{
	cout << __LINE__ << endl;
	Point2f center;
	float radii;
	int fingers = 0;
	minEnclosingCircle(mycontour, center, radii);
	for (int cDefIt = 0; cDefIt < defectsPoints.size(); cDefIt++) {
		int startIndex = defectsPoints[cDefIt].val[0];
		Point StartPoint(mycontour[startIndex]);
		int endIndex = defectsPoints[cDefIt].val[1];
		Point ptEnd(mycontour[endIndex]);
		int farIndex = defectsPoints[cDefIt].val[2];
		Point ptFar(mycontour[farIndex]);
		double depth = static_cast<double>(defectsPoints[cDefIt].val[3]) / 256;
		//displaying start end and far points respectively
		//circle(input, ptStart, 5, CV_RGB(255, 0, 0), 2, 8);
		//circle(input, ptEnd, 5, CV_RGB(255, 255, 0), 2, 8);
		cout << __LINE__ << endl;
		//circle(input, ptFar, 5, CV_RGB(0, 0, 255), 2, 8);
		if (depth > 11 && StartPoint.y < center.y)
		{
			circle(input, StartPoint, 4, CV_RGB(255, 0, 0), 4);
			fingers++;
		}
		switch (fingers)
		{
		
		case 1:  putText(input, to_string(fingers), Point(70, 50), CV_FONT_NORMAL, 1, Scalar(255, 255, 255), 1, 1);
			break;
		case 2:  putText(input, to_string(fingers), Point(90, 50), CV_FONT_NORMAL, 1, Scalar(255, 255, 255), 1, 1);
			break;
		case 3: putText(input, to_string(fingers), Point(110, 50), CV_FONT_NORMAL, 1, Scalar(255, 255, 255), 1, 1);
			break;
		case 4: putText(input, to_string(fingers), Point(130, 50), CV_FONT_NORMAL, 1, Scalar(255, 255, 255), 1, 1);
			break;
		case 5: putText(input, to_string(fingers), Point(150, 50), CV_FONT_NORMAL, 1, Scalar(255, 255, 255), 1, 1);
			break;
		default : putText(input, to_string(fingers), Point(50, 50), CV_FONT_NORMAL, 1, Scalar(255, 255, 255), 1, 1);
			break;
		}

	}
}


