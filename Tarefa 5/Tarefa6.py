#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 11:50:33 2018

@author: robotica
"""
import cv2
import Hough

img = cv2.imread("stuff.jpg",0)

hough = Hough.Circle(img,50,200,50,100,50)
cv2.imwrite("HoughCircle.png",hough)
