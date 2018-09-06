#!/usr/bin/env python
import freenect
import cv2
import frame_convert2
import numpy as np

cv2.namedWindow('Depth')
cv2.namedWindow('Video')
print('Press ESC in window to stop')


def get_depth():
    return frame_convert2.pretty_depth_cv(freenect.sync_get_depth()[0])

def get_depth2():
    return freenect.sync_get_depth()[0]

def get_video():
    return frame_convert2.video_cv(freenect.sync_get_video()[0])

import time
for cont in range (0,120):
    time.sleep(1)
    img = get_video()
	cv2.imwrite("images/"+str(cont)+".png",img)