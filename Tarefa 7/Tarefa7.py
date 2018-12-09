#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 13:28:34 2018

@author: robotica
"""
from PIL import Image
import numpy as np
import math
import cv2
#Recebendo as imagens de Lula e Bolsonaro
img1 = Image.open('baboon.jpg')
img2 = Image.open('lena.jpg')

#Realizando a conversão
img1 = img1.convert('L')
img2 = img2.convert('L')

#Convertendo para Array
a = np.asarray(img1)
b = np.asarray(img2)

cv2.imwrite("baboongray.jpg",a)
cv2.imwrite("lenagray.jpg",b)

# Realizando o fft
#Lula
baboon = np.fft.fft2(a)
baboon = np.fft.fftshift(baboon)
#Bolsonaro
lena = np.fft.fft2(b)
lena = np.fft.fftshift(lena)
#Criando uma imagem de zeros
imagem = np.zeros((img1.size[1],img1.size[0]),dtype=np.complex128)


for u in range(img1.size[0]):
	for v in range(img1.size[1]):
		u1 = u - img1.size[0]/2
		v1 = v - img1.size[1]/2
		Duv = math.sqrt(u1*u1 + v1*v1)
		if Duv > 15:
			imagem[v][u] = lena[v][u]
		else:
			imagem[v][u] = baboon[v][u]

imagem = np.fft.fftshift(imagem)

output = Image.fromarray(np.fft.ifft2(imagem).astype(np.uint8))
output.show()
output.save("imagem.jpg")
