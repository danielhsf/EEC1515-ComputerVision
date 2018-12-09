#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 16:47:21 2018

@author: robotica
"""

import cv2

img = cv2.imread("Louvre.jpg")

fast = cv2.FastFeatureDetector_create()
brief = cv2.xfeatures2d.BriefDescriptorExtractor_create()
kp = fast.detect(img,None)
kp,descbrief = brief.compute(img,kp)

orb = cv2.ORB_create(100000)
kp2 = orb.detect(img)
kp2,descorb = orb.compute(img,kp2) 
