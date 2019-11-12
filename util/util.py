import numpy as np
import cv2

class Util:
	# param 1: image
	@staticmethod
	def mouse_hsvcolor(event, x, y, flags, param):
		if event == cv2.EVENT_LBUTTONDOWN:
			image = param[0]
			# print(type(image))
			# print(image)
			color1 = image[y, x, 0]
			color2 = image[y, x, 1]
			color3 = image[y, x, 2]
			print("1: {}, 2: {}, 3: {}".format(color1, color2, color3))

	@staticmethod
	def detect_edge(channel):
		sobelX = cv2.Sobel(channel, cv2.CV_64F, dx=1, dy=0)
		sobelY = cv2.Sobel(channel, cv2.CV_64F, dx=0, dy=1)
		
		sobelX = cv2.convertScaleAbs(sobelX)
		sobelY = cv2.convertScaleAbs(sobelY)

		sobel = cv2.addWeighted(sobelX, 0.5, sobelY, 0.5, 0)
		return sobel
