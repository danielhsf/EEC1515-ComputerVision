#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 18:22:06 2018

@author: robotica
"""
import numpy as np
import cv2
import os

cap = cv2.VideoCapture('vtest.avi')

for i in range(0,100):
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imwrite("frames3/"+str(i)+".png",frame)

cap.release()


image_folder = 'frames3'
video_name = 'output.avi'

images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
frame = cv2.imread(os.path.join(image_folder, images[0]))

h,w,layers = frame.shape[:]

video = cv2.VideoWriter(video_name, -1, 1, (h,w))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

video.release()