import numpy as np
import cv2
import argparse
from util.divider import Divider
from matplotlib import pyplot as plt

# construct argument parser and parse the argument
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

print("[INFO] starts...")
image = cv2.imread(args["image"])

print("Shape: X: {}; Y: {}".format(image.shape[0], image.shape[1]))
dv = Divider(image, 40, 40)

# def chunkify(img, block_width=4, block_height=4):
#     shape = img.shape
#     x_len = shape[0]//block_width
#     y_len = shape[1]//block_height
#     #print(x_len, y_len)
    
#     chunks = []
#     x_indices = [i for i in range(0, shape[0]+1, block_width)]
#     y_indices = [i for i in range(0, shape[1]+1, block_height)]

#     shapes = list(zip(x_indices, y_indices))
    
#     print(len(y_indices))

#     for i in range(len(shapes)):
#         try:
#             start_x = shapes[i][0]
#             start_y = shapes[i][1]
#             end_x = shapes[i+1][0]
#             end_y = shapes[i+1][1]
#             chunks.append( shapes[start_x:end_x][start_y:end_y] )
#             # tmp_img = img[start_x:end_x, start_y:end_y]
#             # cv2.imshow("Cropped", tmp_img)
#             print("Start X: {}; End X: {}; Start Y: {}; End Y: {}".format(start_x, end_x, start_y, end_y))
#         except IndexError:
#             print('End of Array')

#     cv2.waitKey(0)

#     return chunks

# def chunkify(img, colDivisor=4, rowDivisor=4):
# 	shape = img.shape
# 	x_len = shape[0]
# 	y_len = shape[1]

# 	if(x_len % colDivisor == 0 and y_len % rowDivisor == 0):
		
# 		x_indices = [i for i in range(0, x_len + 1, x_len // colDivisor)]
# 		y_indices = [i for i in range(0, y_len + 1, y_len // rowDivisor)]
		# for x in range(0, x_len + 1, x_len // colDivisor):
		# 	for y in range(0, y_len + 1, y_len // rowDivisor):
		# 		print("X: {}, Y:{}".format(x, y))
		# for x in x_indices:
		# 	print("X: {}".format(x))
		# for y in y_indices:
		# 	print("Y: {}".format(y))

		# for x in x_indices:
		# 	for y in y_indices:
		# 		print("X: {}; Y: {}".format(x, y))


def chunkify(img, colDivisor=4, rowDivisor=4):
	shape = img.shape
	imgWidth = shape[0]
	imgHeight = shape[1]

	x_prev = 0 
	y_prev = 0
	
	ret_coord = []

	if(imgWidth % colDivisor == 0 and imgHeight % rowDivisor == 0):
		x_indices = [i for i in range(0, imgWidth + 1, imgWidth // colDivisor)]
		y_indices = [i for i in range(0, imgHeight + 1, imgHeight // rowDivisor)]

		max_len = max(len(x_indices), len(y_indices))

		for z in range(0, max_len):
			x_coord = x_prev + imgWidth // colDivisor
			y_coord = y_prev + imgHeight // rowDivisor
			
			x_tuple = (x_prev, x_coord)
			y_tuple = (y_prev, y_coord)

			coord = (x_tuple, y_tuple)

			x_prev = x_coord
			y_prev = y_coord 

			ret_coord.append(coord)

	return ret_coord

# image = np.array(image)
blocks = chunkify(image, 5, 5)

for x, y in blocks:
	print("X: {}; Y: {}".format(x, y))

print(image.shape)
# plt.matshow(image)
# plt.show()
cv2.imshow("Image", image)
cv2.waitKey(0)