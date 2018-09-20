#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import math

def Roberts(image,M = "x"):
    h,w = image.shape
    newimg = np.zeros((h-1,w-1), dtype=np.uint8)
    if(M == "x"):
        matrix = np.array([[0,1],[-1,0]])
    elif(M == "y"):
        matrix = np.array([[1,0],[0,-1]])
    for x in range (0,h-2):
        for y in range(0,w-2):
            if(sum(sum(matrix*image[x:x+2,y:y+2])) > 0):
                newimg[x,y] = sum(sum(matrix*image[x:x+2,y:y+2]))
            else:
                newimg[x,y] = 0
    return newimg

def Prewitt(image,M = "x"):
    h,w = image.shape
    newimg = np.zeros((h-2,w-2), dtype=np.uint8)
    if(M == "y"):
        matrix = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
    elif(M == "x"):
        matrix = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
    for x in range (1,h-2):
        for y in range(1,w-2):
            if(sum(sum(matrix*image[x-1:x+2,y-1:y+2])) > 0):
                newimg[x-1,y-1] = sum(sum(matrix*image[x-1:x+2,y-1:y+2]))
            else:
                newimg[x-1,y-1] = 0
    return newimg

def Sobel(image,M = "x"):
    h,w = image.shape
    newimg = np.zeros((h,w), dtype=np.uint8)
    image = np.append([image[0][:]],image,axis =0)
    image = np.append(image,[image[-1][:]],axis =0)
    image = np.append(np.transpose([image[:,0]]),image, axis=1)
    image = np.append(image, np.transpose([image[:,-1]]), axis=1)
    if(M == "x"):
        matrix = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
    elif(M == "y"):
        matrix = np.array([[1,2,1],[0,0,0],[-1,-2,-1]])
    for x in range (0,h):
        for y in range(0,w):
            if(sum(sum(matrix*image[x:x+3,y:y+3])) > 0):
                if(sum(sum(matrix*image[x:x+3,y:y+3])) > 255):
                    newimg[x,y] = 255
                else:
                    newimg[x,y] = sum(sum(matrix*image[x:x+3,y:y+3]))
            else:
                newimg[x,y] = 0
    return newimg

def Laplacian(image):
    h,w = image.shape
    newimg = np.zeros((h,w), dtype=np.uint8)
    image = np.append([image[0][:]],image,axis =0)
    image = np.append(image,[image[-1][:]],axis =0)
    image = np.append(np.transpose([image[:,0]]),image, axis=1)
    image = np.append(image, np.transpose([image[:,-1]]), axis=1)
    matrix = np.array([[0,-1,0],[-1,4,-1],[0,-1,0]])
    for x in range (0,h):
        for y in range(0,w):
            if(sum(sum(matrix*image[x:x+3,y:y+3])) > 0):
                if(sum(sum(matrix*image[x:x+3,y:y+3])) > 255):
                    newimg[x,y] = 255
                else:
                    newimg[x,y] = sum(sum(matrix*image[x:x+3,y:y+3]))
            else:
                newimg[x,y] = 0
    return newimg

def Median(image):
    newimg = np.copy(image)
    h,w = image.shape
    for x in range (1,h-1):
        for y in range(1,w-1):
            a = image[x-1:x+2,y-1:y+2]
            a = a.flatten()
            a.sort()
            newimg[x,y] = a[4]
    return newimg

def Mean(image):
    h,w = image.shape
    newimg = np.zeros((h-2,w-2), dtype=np.uint8)
    for x in range (1,h-2):
        for y in range(1,w-2):
            a = image[x-1:x+2,y-1:y+2]
            newimg[x-1,y-1] = a.mean(dtype= np.uint64)
    return newimg

def Gaussian(image):
    h,w = image.shape
    newimg = np.zeros((h,w), dtype=np.uint8)
    image = np.append([image[0][:]],image,axis =0)
    image = np.append(image,[image[-1][:]],axis =0)
    image = np.append(np.transpose([image[:,0]]),image, axis=1)
    image = np.append(image, np.transpose([image[:,-1]]), axis=1)
    matrix = np.array([[1,2,1],[2,4,2],[1,2,1]])
    for x in range (0,h):
        for y in range(0,w):
            if(int(sum(sum(matrix*image[x:x+3,y:y+3]))/16) > 0):
                newimg[x,y] = int(sum(sum(matrix*image[x:x+3,y:y+3]))/16)
            else:
                newimg[x,y] = 0
    return newimg

def Gaussian2(image):
    h,w = image.shape
    newimg = np.copy(image)
    image = np.append([image[0][:]],image,axis =0)
    image = np.append([image[0][:]],image,axis =0)
    image = np.append(image,[image[-1][:]],axis =0)
    image = np.append(image,[image[-1][:]],axis =0)
    image = np.append(np.transpose([image[:,0]]),image, axis=1)
    image = np.append(np.transpose([image[:,0]]),image, axis=1)
    image = np.append(image, np.transpose([image[:,-1]]), axis=1)
    image = np.append(image, np.transpose([image[:,-1]]), axis=1)
    matrix = np.array([[2,4,5,4,2],[4,9,12,9,4],[5,12,15,12,5],[4,9,12,9,4],[2,4,5,4,2]])
    for x in range (2,h+2):
        for y in range(2,w+2):
            newimg[x-2,y-2] = int(sum(sum(matrix*image[x-2:x+3,y-2:y+3]))/159)
    return newimg

def choice(img,x,y,i,f):
    value = img[x,y]
    if(value<i):
        return 0
    elif(value<f):
        return i
    else:
        return f

def suprimir(img,x,y,ang):
    if(ang == 0):
        if((img[x,y]>img[x,y+1]) and (img[x,y]>=img[x,y-1])):
            return img[x,y] 
        else:
            return 0
    elif(ang == 45):
        if((img[x,y]>img[x+1,y-1]) and (img[x,y]>img[x-1,y+1])):
            return img[x,y]
        else:
            return 0
    elif(ang == 90):
        if((img[x,y]>img[x+1,y]) and (img[x,y]>=img[x-1,y])):
            return img[x,y]
        else:
            return 0
    elif(ang == 135):
        if((img[x,y]>img[x-1,y-1]) and (img[x,y]>img[x+1,y+1])):
            return img[x,y]
        else:
            return 0
        
def Canny(image,t1,t2):
    Gaussiana = np.copy(image)
    Gaussiana = Gaussian(Gaussiana)
    Laplaciano = np.sqrt(Laplacian(Gaussiana))
    h,w = Gaussiana.shape
    Gx = Sobel(Gaussiana,"x")
    Gy = Sobel(Gaussiana,"y")
    theta = np.arctan2(Gy,Gx)
    theta[np.isnan(theta)]= 0
    t = np.copy(theta)
    #Non-max supression
    for x in range (0,h):
        for y in range(0,w):
            if(theta[x,y]<=math.pi/8):
                t[x,y] = 0
            elif(theta[x,y]<=3*math.pi/8):
                t[x,y] = 45
            elif(theta[x,y]<=5*math.pi/8):
                t[x,y] = 90
            elif(theta[x,y]<=7*math.pi/8):
                t[x,y] = 135
            else:
                t[x,y] = 0
    temp = np.zeros((h,w), dtype=np.uint8)
    for x in range (1,h-1):
        for y in range(1,w-1):
            temp[x,y] =  suprimir(Laplaciano,x,y,t[x,y])
    temp[:,0] = temp[:,1]
    temp[:,-1] = temp[:,-2]
    temp[0,:] = temp[1,:]
    temp[-1,:] = temp[-2,:]
    
    #Normalizando
    Laplaciano = (255/np.max(Laplaciano))*Laplaciano
    # Double Thresholnding
    #a)
    classifier = np.zeros((h,w))
    for x in range (0,h):
        for y in range(0,w):
            if(Laplaciano[x,y]<t1):
                classifier[x,y] = 0
            elif(Laplaciano[x,y]<t2):
                classifier[x,y] = 1
            else:
                classifier[x,y] = 2
    #b) 
    supression = np.zeros((h,w), dtype=np.uint8)     
    for x in range (1,h-1):
        for y in range(1,w-1):
            if(classifier[x,y] == 0):
                supression[x,y] = 0
            elif(classifier[x,y] == 1):
                aux = classifier[x-1:x+2,y-1:y+2]
                if((aux == 0).sum() == 8):
                    supression[x,y] = 0
                else:
                    supression[x,y] = 255
            else:
                supression[x,y] = 255
    return Gx,Gy,theta,Gaussiana,Laplaciano,supression

def Laplacian2(image,h,w):
    newimg = np.copy(image)
    matrix = np.array([[0,1,0],[1,-4,1],[0,1,0]])
    for x in range (1,h-2):
        for y in range(1,w-2):
            newimg[x,y] = sum(sum(matrix*image[x-1:x+2,y-1:y+2]))
    return newimg