#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img1 = cv.imread("football_ball.jpg")
img2 = cv.imread("baseball_ball.png")

img1 = cv.resize(img1,(1024,1024))
img2 = cv.resize(img2,(1024,1024))

rows = 1024
cols = 1024

#Reduzindo a primeira vez
g11 = cv.pyrDown(img1, dstsize=(cols // 2, rows // 2))
g12 = cv.pyrDown(img2, dstsize=(cols // 2, rows // 2))

#Reduzindo a segunda vez
g21 = cv.pyrDown(g11, dstsize=(cols // 4, rows // 4))
g22 = cv.pyrDown(g12, dstsize=(cols // 4, rows // 4))

#Reduzindo a terceira vez
g31 = cv.pyrDown(g21, dstsize=(cols // 8, rows // 8))
g32 = cv.pyrDown(g22, dstsize=(cols // 8, rows // 8))

#Ampliando a primeira vez
l11 = cv.pyrUp(g31, dstsize=(cols // 4, rows // 4))
l12 = cv.pyrUp(g32, dstsize=(cols // 4, rows // 4))

#Ampliando a primeira vez
l21 = cv.pyrUp(l11, dstsize=(cols // 2, rows // 2))
l22 = cv.pyrUp(l12, dstsize=(cols // 2, rows // 2))

#Ampliando a segunda vez
l31 = cv.pyrUp(l21, dstsize=(cols, rows))
l32 = cv.pyrUp(l22, dstsize=(cols, rows))

#Fundindo as metades 
final = np.zeros((rows,cols,3),dtype=np.uint8)
final[0:rows,0:cols//2] = l31[0:rows,0:cols//2]

final[0:rows,cols//2:cols] = l32[0:rows,cols//2:cols]

cv.imwrite("Saida.png",final)


