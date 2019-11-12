# use this class to split original image into smaller chunks
# USAGE
# python process.py -i data.jpg

import numpy as np
import cv2
import argparse
from util.divider import Divider

# construct argument parser and parse the argument
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

print("[INFO] starts...")
image = cv2.imread(args["image"])

print("Shape: X: {}; Y: {}".format(image.shape[0], image.shape[1]))
dv = Divider(5, 6)
img = dv.pad_image(image)
# print("Shape 1: X: {}; Y: {}".format(img.shape[0], img.shape[1]))
coord = dv.get_chunk_coord(img)
dv.slice_image(img, coord)
