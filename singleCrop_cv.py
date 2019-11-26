# USAGE
# python singleCrop_cv.py
# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_template_matching/py_template_matching.html

import cv2
import numpy as np
import imutils
from matplotlib import pyplot as plt

# image = cv2.imread('Rst/OlivoTotal.png')
# template = cv2.imread('Rst/OlivoTemplate_small.png',0)
image = cv2.imread('output/1.jpg')
template = cv2.imread('template/1.jpg',0)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

w, h = template.shape[::-1]

res = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.3
loc = np.where(res >= threshold)

for pt in zip(*loc[::-1]):
        cv2.rectangle(image, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

image = imutils.resize(image, width=800)
cv2.imshow("image", image)
cv2.waitKey(0)
