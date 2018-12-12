#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import Hough
import cv2

image,m = Hough.Line("stuff.jpg",50,200,50)

cv2.imwrite("saida.png",image)