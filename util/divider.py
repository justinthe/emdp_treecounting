import numpy as np
import cv2

class Divider:
    def __init__(self,image, block_width, block_height):
        self.block_width = block_width
        self.block_height = block_height
        self.image = image

    def chunkify(self):
        shape = self.image.shape
        x_len = shape[0] // self.block_width
        y_len = shape[1] // self.block_height
        print("x_len: {}; y_len: {}".format(x_len, y_len))

        chunks = []
        x_indices = [i for i in range(0, shape[0] + 1, self.block_width)]
        y_indices = [i for i in range(0, shape[1] + 1, self.block_height)]

        shapes = list(zip(x_indices, y_indices))

        for i in range(len(shapes)):
            try:
                start_x = shapes[i][0]
                start_y = shapes[i][1]
                end_x = shapes[i+1][0]
                end_y = shapes[i+1][1]
                chunks.append(shapes[start_x:end_x][start_y:end_y])
            except IndexError:
                print('End of Array')

        return chunks

    
