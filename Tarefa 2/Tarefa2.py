#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 13:34:41 2018

@author: robotica
"""
import filters
import cv2
import numpy as np

image = cv2.imread("lena.jpg",0)
cv2.imwrite("blackLena.jpg",image)
#Aplicando o Filtro de Roberts Gx e Gy
#Gx
#Usando Filter2D do Opencv
dst = cv2.filter2D(image,-1,np.array([[0,1],[-1,0]]))
cv2.imwrite("RobertsGx-Opencv.jpg",dst)
#Implementando via numpy
newimg = filters.Roberts(image,"x")
cv2.imwrite("RobertsGx.jpg",newimg)
#Gy
#Usando Filter2D do Opencv
dst = cv2.filter2D(image,-1,np.array([[1,0],[0,-1]]))
cv2.imwrite("RobertsGy-Opencv.jpg",dst)
#Implementando via numpy
newimg = filters.Roberts(image,"y")
cv2.imwrite("RobertsGy.jpg",newimg)

#Aplicando o Filtro De Prewitt
#Gx
#Usando Filter2D do Opencv
dst = cv2.filter2D(image,-1,np.array([[-1,0,1],[-1,0,1],[-1,0,1]]))
cv2.imwrite("PrewittGx-Opencv.jpg",dst)
#Implementando via Numpy
newimg = filters.Prewitt(image,"x")
cv2.imwrite("PrewittGx.jpg",newimg)
#Usando Filter2D do Opencv
dst = cv2.filter2D(image,-1,np.array([[1,1,1],[0,0,0],[-1,-1,-1]]))
cv2.imwrite("PrewittGy-Opencv.jpg",dst)
#Implementando via Numpy
newimg = filters.Prewitt(image,"y")
cv2.imwrite("PrewittGy.jpg",newimg)

#Aplicando o Filtro de Sobel
#Gx
dst = cv2.filter2D(image,-1,np.array([[-1,0,1],[-2,0,2],[-1,0,1]]))
cv2.imwrite("SobelGx-OpenCV.jpg",dst)
newimg = filters.Sobel(image,"x")
cv2.imwrite("SobelGx.jpg",newimg)
#Gy
dst = cv2.filter2D(image,-1,np.array([[1,2,1],[0,0,0],[-1,-2,-1]]))
cv2.imwrite("SobelGy-OpenCV.jpg",dst)
newimg = filters.Sobel(image,"y")
cv2.imwrite("SobelGy.jpg",newimg)

#Laplaciano
dst = cv2.filter2D(image,-1,np.array([[0,-1,0],[-1,4,-1],[0,-1,0]]))
cv2.imwrite("Laplacian-OpenCV.jpg",dst)
newimg = filters.Laplacian(image)
cv2.imwrite("Laplacian.jpg",newimg)

#Canny
image = cv2.imread("lena.jpg",0)
t1 = filters.Canny(image)
cv2.imwrite("Canny.jpg",t1)
ref = cv2.Canny(image,0,0)
cv2.imwrite("Canny-OpenCV.jpg",ref)


#Média
dst = cv2.filter2D(image,-1,np.array([[1,1,1],[1,1,1],[1,1,1]])/9)
cv2.imwrite("Mean-OpenCV.jpg",dst)
newimg = filters.Mean(image)
cv2.imwrite("Mean.jpg",newimg)
#Mediana
image = cv2.imread("lena_saltpepper.png",0)
dst = cv2.medianBlur(image,3)
cv2.imwrite("Median-Opencv.jpg",dst)
newimg = filters.Median(image)
cv2.imwrite("Median.jpg",newimg)
#Gaussiana
dst = cv2.filter2D(image,-1,np.array([[1,2,1],[2,4,2],[1,2,1]])/16)
cv2.imwrite("Gaussian-OpenCV.jpg",dst)
newimg = filters.Gaussian(image)
cv2.imwrite("Gaussian.jpg",newimg)


