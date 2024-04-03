import os

from stitching import Stitcher

import cv2
import time

# img_dir = r'./test_imgs'
img_dir =  r"./test_data/layer-02"
img_list = [cv2.imread(os.path.join(img_dir,i)) for i in os.listdir(img_dir)] # [:2]

stitcher = Stitcher(crop=False)
t0 = time.time()
panorama = stitcher.stitch(img_list)
print('cast-time:',time.time()-t0)
cv2.imwrite('res-hsc-layer-test.png', panorama)