# use this class to get color range before running get_contour.py
# USAGE
# python get_color_range.py -i output/1.jpg

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

print("Shape: X: {}; Y: {}".format(image.shape[0], image.shape[1]))
image = imutils.resize(image, width=750)
print("Shape 1: X: {}; Y: {}".format(image.shape[0], image.shape[1]))

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


lower_green = (36, 25, 25)
upper_green = (70, 255, 255)
mask = cv2.inRange(hsv, lower_green, upper_green)

target = cv2.bitwise_and(image, image, mask = mask)
# cv2.imshow("Masked", target)
# cv2.waitKey(0)

# print(type(image))
# print(len(image))

cv2.namedWindow("mouse_event")

param = [image]
cv2.setMouseCallback("mouse_event", Util.mouse_hsvcolor, param)

while True:
	cv2.imshow("mouse_event", image)
	if cv2.waitKey(1) & 0xFF == ord("q"):
		break

cv2.destroyAllWindows()