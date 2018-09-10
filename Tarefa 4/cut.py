import cv2
import numpy as np
 
# Read image
im = cv2.imread("volkswagen.jpg")
     
# Select ROI
r = cv2.selectROI(im)
# Crop image
imCrop = im[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
 
# Display cropped image
cv2.imwrite("mask.jpg",imCrop)
