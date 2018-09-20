#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import Hough
import cv2

image,m = Hough.Line("building.jpg",150,200,500)

cv2.imwrite("saida.png",image)