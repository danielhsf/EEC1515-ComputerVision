#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 15:35:19 2018

@author: robotica
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

#Lendo a Imagem Original
img = cv2.imread('volkswagen.jpg',0)
color = cv2.imread('volkswagen.jpg')

#Lendo o Template 
templ = cv2.imread('template.jpg',0)


strings = ['SQDIFF', 'SQDIFF NORMED', 'TM CCORR', 'TM CCORR NORMED', 'TM COEFF', 'TM COEFF NORMED']
match_method = [cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED, cv2.TM_CCORR,cv2.TM_CCORR_NORMED, cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED]

for i in range(0,6):
    color = cv2.imread('volkswagen.jpg')
    
    result = cv2.matchTemplate(img, templ, match_method[i])
    
    ## [normalize]
    cv2.normalize( result, result, 0, 1, cv2.NORM_MINMAX, -1 )
    ## [normalize]
    ## [best_match]
    _minVal, _maxVal, minLoc, maxLoc = cv2.minMaxLoc(result, None)
    ## [best_match]

    ## [match_loc]
    if (match_method[i] == cv2.TM_SQDIFF or match_method[i] == cv2.TM_SQDIFF_NORMED):
        matchLoc = minLoc
    else:
        matchLoc = maxLoc
    ## [match_loc]
    
    ## [imshow]
    print("Printando")
    print(matchLoc)
    cv2.rectangle(color, matchLoc, (matchLoc[0] + templ.shape[0], matchLoc[1] + templ.shape[1]), (0,0,255), 2, 8, 0 )
    cv2.rectangle(result, matchLoc, (matchLoc[0] + templ.shape[0], matchLoc[1] + templ.shape[1]), (0,0,255), 2, 8, 0 )
    cv2.imwrite(strings[i]+".jpg", color)
    #cv2.imshow("Resultadodomatching.jpg", result)