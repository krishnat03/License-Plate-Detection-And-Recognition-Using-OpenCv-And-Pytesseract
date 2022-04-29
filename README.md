# License-Plate-Detection-And-Recognition-Using-OpenCv-And-Pytesseract
License plate detection is identifying the part of the car that is predicted to be the number plate. Recognition is identifying the values that make up the license plate.

License plate detection and recognition is the technology that uses computer vision to detect and recognize a license plate from an input image of a car.

This technology applies in many areas. On roads, it is used to identify the cars that are breaking the traffic rules. In security, it is used to capture the license plates of the vehicles getting into and out of certain premises. In parking lots, it is used to capture the license plates of the cars being parked. The list of its applications goes on and on.

# Introduction
Python gives us the ability to create our license plate detection and recognition program. We achieve this by using three of its libraries; pytesseract, imutils, and OpenCv.

# Processes a software undergoes to detect and recognize a license plate
For software to detect and recognize a license plate, it undergoes three major processes.
 1. <strong>Taking an image of a car as input</strong> - The program takes in the input of the car in which the license plate is to be detected.
 2. <strong>Processing the input</strong> - The image taken as the input undergoes processing to detect the part of the car that is the license plate.
 3. <strong>Recognizing the number plate</strong> - The values of the detected license plate are extracted from the number plate image.

# Creating a license plate detection and recognition program
I'm using Pycharm for this project.
First things first, You have to download tesseract(This is software that will use to recognize characters from an image) and install it. And then in terminal section of Pycharm we will install 3 things i.e
 1. pip install opencv-contrib-python  (We also refer to this library as cv2. We will use it to preprocess our image and also display the images that have undergone processing.)
 2. pip install imutils (We will need this library to resize our images.)
 3. pip install pytesseract (We will need this library to extract the license plate text from the detected license plate.)
