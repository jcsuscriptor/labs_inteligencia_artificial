# import the necessary packages
import numpy as np
import argparse
import cv2

# Load an color image in grayscale
# 0 o cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
image = cv2.imread('img4.jpg') #,0)

#Display an image
#cv2.imshow('image',image)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

output = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# detect circles in the image
#circles = cv2.HoughCircles(gray, cv2.cv.CV_HOUGH_GRADIENT, 1.2, 100)
#circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,20,
#                            param1=50,param2=30,minRadius=0,maxRadius=0)

circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1.2,50)

# ensure at least some circles were found
if circles is not None:
	# convert the (x, y) coordinates and radius of the circles to integers
	circles = np.round(circles[0, :]).astype("int")
 
	# loop over the (x, y) coordinates and radius of the circles
	for (x, y, r) in circles:
		# draw the circle in the output image, then draw a rectangle
		# corresponding to the center of the circle
		cv2.circle(output, (x, y), r, (0, 255, 0), 4)
		cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
 
	# show the output image
	cv2.imshow("output", np.hstack([image, output]))
	cv2.waitKey(0)
 