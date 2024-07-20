import sys
import cv2
import glob
import numpy as np
import matplotlib.pyplot as plt

im_depth = cv2.imread('depth_0016.png', -1)

plt.subplot(1, 2, 1)
plt.imshow(im_depth)

x = 200
y = 0
h_x =400
h_y=300
im_crop = im_depth#[y:y+h_y, x:x+h_x]
im_crop[im_crop > 1000] = 1000 
im_crop[im_crop < 2] = 0
im_crop = im_crop.astype(np.float32)

plt.subplot(1, 2, 2)
plt.imshow(im_crop)

plt.show()