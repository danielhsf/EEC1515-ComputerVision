#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 14:44:30 2018

@author: robotica
"""
import cv2
import numpy as np

#Estudando a Correlação 
BancoDeImagens = np.zeros((100,480,640),dtype=np.uint8) 
for n in range(19,119):
    img = cv2.imread("images/"+str(n)+".png",0)
    #img	= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #cv2.imwrite("images/"+str(n),img) 
    BancoDeImagens[n-19] = img
    
line0 = BancoDeImagens[:,0,0]
correlation = np.zeros((480),dtype = np.float64) 

for i in range(0,480):
    newline = BancoDeImagens[:,0,i]
    correlation[i] = np.corrcoef(line0,newline)[0][1]
    
import matplotlib.pyplot as plt
plt.xlabel('Proximidade entre os Pixels')
plt.ylabel('Grau de Correlação')
plt.title('Correlação entre pixels')
plt.plot(correlation)
pl1 = plt.plot(correlation[0],'o')
plt.grid(True)
plt.show()
plt.savefig("correlation.png")
plt.show()