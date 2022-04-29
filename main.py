#########################################################################################
# Engineer: Krishna Thakur                                                              #
# Create Date:   04/29/2022                                                             #
# Design Name:   Licence Plate Detection                                                #
# Project Name:  License Plate Detection And Recognition Using OpenCv And Pytesseract   #
#########################################################################################

import cv2
import imutils
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Read the image file
image = cv2.imread('Car Images/hr.jpg')

# Resize the image - change width to 500
image = imutils.resize(image, width=300)

# Display the original image
cv2.imshow("Original Image", image)
cv2.waitKey(0)

# RGB to Gray scale conversion
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("greyed image", gray_image)
cv2.waitKey(0)

# Noise removal with iterative bilateral filter(removes noise while preserving edges)
gray_image = cv2.bilateralFilter(gray_image, 11, 17, 17)
cv2.imshow("smoothened image", gray_image)
cv2.waitKey(0)

# Find Edges of the grayscale image
edged = cv2.Canny(gray_image, 30, 200)
cv2.imshow("edged image", edged)
cv2.waitKey(0)

# Find contours based on Edges
cnts, new = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# Create copy of original image to draw all contours
image1 = image.copy()
cv2.drawContours(image1, cnts, -1, (0, 255, 0), 3)
cv2.imshow("contours", image1)
cv2.waitKey(0)

# sort contours based on their area keeping minimum required area as '30'
# (anything smaller than this will not be considered)
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:30]
screenCnt = None  # we currently have no Number plate contour

# Top 30 Contours
image2 = image.copy()
cv2.drawContours(image2, cnts, -1, (0, 255, 0), 3)
cv2.imshow("Top 30 contours", image2)
cv2.waitKey(0)

# loop over our contours to find the best possible approximate contour of number plate
i = 8
for c in cnts:
    perimeter = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * perimeter, True)
    # print ("approx = ",approx)
    if len(approx) == 4:  # Select the contour with 4 corners
        screenCnt = approx  # This is our approx Number Plate Contour

        # Crop those contours and store it in Cropped Images folder
        x, y, w, h = cv2.boundingRect(c)  # This will find out co-ord for plate
        new_img = image[y:y + h, x:x + w]  # Create new image
        cv2.imwrite('Cropped Images-Text/' + str(i) + '.png', new_img)  # Store new image
        i += 1

        break


# Drawing the selected contour on the original image
# print(screenCnt)
cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 3)
cv2.imshow("image with detected license plate", image)
cv2.waitKey(0)

Cropped_loc = 'Cropped Images-Text/8.png'
cv2.imshow("cropped", cv2.imread(Cropped_loc))

# Use tesseract to covert image into string
plate = pytesseract.image_to_string(Cropped_loc, lang='eng')
print("Number plate is:", plate)
cv2.waitKey(0)  # Wait for user input before closing the images displayed
