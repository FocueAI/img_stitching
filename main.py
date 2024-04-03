from stitching import AffineStitcher
import cv2,os
import time

img_dir =  r"./test_data/layer-02"
img_list = [cv2.imread(os.path.join(img_dir,i)) for i in os.listdir(img_dir)]

stitcher = AffineStitcher(crop=False,confidence_threshold=1)

t0 = time.time()
panorama = stitcher.stitch(img_list)
print('cast-time:',time.time()-t0)
cv2.imwrite('res-layer-test.png', panorama)