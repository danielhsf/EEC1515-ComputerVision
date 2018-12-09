#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2
import numpy as np
import math

def Line(img,t1,t2,lim):
    img = cv2.imread(img,0)
    h,w = img.shape[:]
    print("Altura "+str(h)+" "+"Largura "+str(w))
    pmax = int(math.sqrt(h**2 + w**2))
    print("P máximo "+str(pmax))
    M = np.zeros((int(pmax/5+1),36))
    lines = cv2.Canny(img,t1,t2)
    for x in range (0,h):
        for y in range(0,w):
            if(lines[x,y] == 255): 
                    for theta in range(0,180,5):
                        p = x*math.cos(math.pi*theta/180) + y*math.sin(math.pi*theta/180)
                        M[int(round(p,0)/5),int(theta/5)]+=1
                    
    pmax,t = np.unravel_index(M.argmax(), M.shape)
    output = cv2.cvtColor(lines,cv2.COLOR_GRAY2BGR)
    print("Limite "+str(lim))
    while(M[pmax,t]>lim):
        for x in range (0,h):
            for y in range(0,w):
                value = x*math.cos(math.pi*t*5/180) + y*math.sin(math.pi*t*5/180) - pmax*5
                if(int(round(value,0)) == 0):
                    output[x,y] = np.array([0, 0, 255], dtype=np.uint8)
        print(M[pmax,t])
        M[pmax,t] = 0
        pmax,t = np.unravel_index(M.argmax(), M.shape)
    return output,M

def Circle(img,t1,t2,r,R,votos):
    h,w = img.shape[:]
    canny = cv2.Canny(img,t1,t2)
    M = np.zeros((h+1,w+1,R-r))
    for x in range(0,h):
        for y in range(0,w):
            if(canny[x,y] == 255):
                print(str((x*y)/(h*w)))
                for raio in range(r,R):
                    for a in range(0,h):
                        for b in range(0,w):
                            value = ((x-a)**2 + (y-b)**2) == raio**2
                            if(value):
                                M[a,b,raio-r]+=1
    altura,largura,raio = np.unravel_index(M.argmax(), M.shape) 
    print("Altura: "+str(altura)+" Largura: "+str(largura)+" Raio: "+str(raio+r))
    print(M[altura,largura,raio])
    output = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
    while(M[altura,largura,raio]> votos):
        for t in range(0,360):
            x = altura + (raio+r)*math.cos(t*math.pi/180)
            y = largura + (raio+r)*math.sin(t*math.pi/180)
            output[int(round(x)),int(round(y))] = np.array([0, 0, 255], dtype=np.uint8)
        print("Altura: "+str(altura)+" Largura: "+str(largura)+" Raio: "+str(raio+r))
        print(M[altura,largura,raio])
        M[altura,largura,raio] = 0
        altura,largura,raio = np.unravel_index(M.argmax(), M.shape) 
    return output