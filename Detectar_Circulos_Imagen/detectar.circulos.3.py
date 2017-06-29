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
#circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,20)

#Default: double param1=100, double param2=100, int min_radius=0, int max_radius=0
circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,20,
                           param1=50,param2=50,minRadius=0,maxRadius=0)

# ensure at least some circles were found
if circles is not None:
	# convert the (x, y) coordinates and radius of the circles to integers
	circles = np.round(circles[0, :]).astype("int")
	# loop over the (x, y) coordinates and radius of the circles
	for (x, y, r) in circles:
		 # draw the outer circle
		cv2.circle(output,(x,y),r,(0,255,0),2)
		# draw the center of the circle
		cv2.circle(output,(x,y),2,(0,0,255),3)

	cv2.imshow('detected circles',output)
	cv2.waitKey(0)
	cv2.destroyAllWindows()	
else:
	print("No existe circles")