#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2
import numpy as np

#Criando nosso vetor 
BancoDeImagens = np.zeros((100,480,640),dtype=np.uint8) 
i = 0
for n in range(19,120):
    img = cv2.imread("images/"+str(n)+".png",0)
    BancoDeImagens[i-19] = img
    i+=1

#Calculando a média das imagens    
newimg = np.mean(BancoDeImagens, axis=0)    
cv2.imwrite("media.png",newimg) 

#Calculando o Desvio Padrão
standardDeviation = np.std(BancoDeImagens, axis = 0)
standardDeviation = np.around(standardDeviation)
standardDeviation = standardDeviation.astype(np.uint8)
cv2.imwrite("desvio.png",standardDeviation) 
#Normalizando o Resultado
standardDeviation = (255/np.amax(standardDeviation))*standardDeviation
cv2.imwrite("desvioNormalizado.png",standardDeviation) 


