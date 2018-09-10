#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img1 = cv.imread("9.jpg",0)
img2 = cv.imread("10.jpg",0)

rows, cols = map(int, img1.shape)

#Reduzindo a primeira vez
g11 = cv.pyrDown(img1, dstsize=(cols // 2, rows // 2))
g12 = cv.pyrDown(img2, dstsize=(cols // 2, rows // 2))

#Reduzindo a segunda vez
g21 = cv.pyrDown(g11, dstsize=(cols // 4, rows // 4))
g22 = cv.pyrDown(g12, dstsize=(cols // 4, rows // 4))

#Ampliando a primeira vez
l11 = cv.pyrUp(g21, dstsize=(cols // 2, rows // 2))
l12 = cv.pyrUp(g22, dstsize=(cols // 2, rows // 2))

#Ampliando a segunda vez
l21 = cv.pyrUp(l11, dstsize=(cols, rows))
l22 = cv.pyrUp(l12, dstsize=(cols, rows))

#Fundindo as metades 
final = np.zeros((rows,cols),dtype=np.uint8)
final[0:rows,0:cols//2] = l21[0:rows,0:cols//2]

final[0:rows,cols//2:cols] = l22[0:rows,cols//2:cols]

cv.imwrite("Saida.png",final)


