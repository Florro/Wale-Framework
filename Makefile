all: test
test: test.cpp 
	g++ test.cpp -lopencv_core -lopencv_objdetect -lopencv_highgui -lopencv_imgcodecs -lopencv_imgproc -o test 