import numpy as np
import cv2

class Divider:
    def __init__(self, colDivisor, rowDivisor):
        self.colDivisor = colDivisor
        self.rowDivisor = rowDivisor

    def get_chunk_coord(self, image):
        shape = image.shape
        imgWidth = shape[0]
        imgHeight = shape[1]

        x_prev = 0 
        y_prev = 0
        
        ret_coord = []
        
        if(imgWidth % self.colDivisor == 0 and imgHeight % self.rowDivisor == 0):
            x_indices = [i for i in range(0, imgWidth + 1, imgWidth // self.colDivisor)]
            y_indices = [i for i in range(0, imgHeight + 1, imgHeight // self.rowDivisor)]

            max_len = max(len(x_indices), len(y_indices))

            x_sets = set()
            y_sets = set()

            for z in range(0, max_len):
                x_coord = x_prev + imgWidth // self.colDivisor
                y_coord = y_prev + imgHeight // self.rowDivisor
                
                # make sure we dont get coordinate > dan img width and/or height
                x_tuple = (min(x_prev, (imgWidth - 1)), min(x_coord, (imgWidth - 1)))
                y_tuple = (min(y_prev, (imgHeight - 1)), min(y_coord, (imgHeight - 1)))

                x_sets.add(x_tuple)
                y_sets.add(y_tuple)
                
                x_prev = x_coord
                y_prev = y_coord 


            ret_coord.append((list(x_sets), list(y_sets)))

        return ret_coord

    def slice_image(self, image, ret_coord):
        for x_coords, y_coords in ret_coord:
            # print("X: {}; Y: {}".format(x_coords, y_coords))
            for x in x_coords:
                for y in y_coords:
                    print("X: {}; Y: {}".format(x, y))
                    crop_image = image[x[0]:x[1], y[0]:y[1]]
                    filename = "{}_{}.jpg".format(x, y)
                    cv2.imwrite(filename, crop_image)

    
    def pad_image(self, image):
        shape = image.shape
        imgWidth = shape[0]
        imgHeight = shape[1]

        x_val = int(imgWidth // self.colDivisor) + 1
        y_val = int(imgHeight //  self.rowDivisor) + 1
        # print(x_val, y_val)

        x_target = (self.colDivisor * x_val) - imgWidth
        y_target = (self.rowDivisor * y_val) - imgHeight
        # print(x_target, y_target)

        left = x_target // 2
        right = x_target - left

        top = y_target // 2
        bottom = y_target - top

        # print(top, bottom, left, right)
        ret_image = cv2.copyMakeBorder(
                            image, 
                            top, 
                            bottom, 
                            left, 
                            right, 
                            cv2.BORDER_CONSTANT, 
                            value=(0.0, 0.0, 0.0)
                            )
        ret_image = cv2.resize(ret_image, (imgHeight + y_target, imgWidth + x_target))
        # print(ret_image.shape[0], ret_image.shape[1])
        
        return ret_image