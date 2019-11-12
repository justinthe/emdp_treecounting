# USAGE
# python get_contour.py -i output/1.jpg

import numpy as np
import cv2
import argparse
import imutils
from util.util import Util
from matplotlib import pyplot as plt


# construct argument parser and parse the argument
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

print("[INFO] starts...")
image = cv2.imread(args["image"]) 
image = imutils.resize(image, width=750)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_green = (50, 50, 50)
upper_green = (80, 150, 150)
mask = cv2.inRange(hsv, lower_green, upper_green)

target = cv2.bitwise_and(image, image, mask = mask)
# cv2.imshow("Masked", target)
# cv2.waitKey(0)

gray = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (3, 3), 0)
# cv2.dilate(blurred, None, iterations = 3)
cv2.erode(blurred, None, iterations = 1)
edgeImg = Util.detect_edge(blurred)

cnts = cv2.findContours(edgeImg, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

cv2.drawContours(image, cnts, -1, (0, 0, 255), 2)

cv2.imshow("Image", image)
cv2.imshow("Edge Image", target)
cv2.waitKey(0)



# print(type(image))
# print(len(image))

