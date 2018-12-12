#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2
import skvideo.io

def valid_p(i, j, height, width):
    return (i >= 0 and i < height) and (j >= 0 and j < width)

out = skvideo.io.FFmpegWriter("slow.mp4")
origin = skvideo.io.FFmpegWriter("real.mp4")


#Reading the video
#cap = cv2.VideoCapture("vtest.avi")
cap = cv2.VideoCapture("videoplayback.mp4")


#Capturing the old frame
ret, old_frame = cap.read()
old_frame = cv2.cvtColor(old_frame,cv2.COLOR_BGR2GRAY)
h,w = old_frame.shape[:]
cv2.imwrite("Real/0.png",old_frame)
cv2.imwrite("Slow/0.png",old_frame)
out.writeFrame(old_frame)
origin.writeFrame(old_frame)
# Define the codec and create VideoWriter object

for cont in range(0,350):
    print(cont)
    #Capturing the new frame
    ret, new_frame = cap.read()
    if(ret == False):
        break
    new_frame = cv2.cvtColor(new_frame,cv2.COLOR_BGR2GRAY)
    flow = cv2.calcOpticalFlowFarneback(old_frame,new_frame, None, 0.5, 3, 15, 3, 5, 1.2, 0)
    
    x0 = flow[...,0]/3
    y0 = flow[...,1]/3
    
    x1 = 2*flow[...,0]/3
    y1 = 2*flow[...,1]/3
    
    x0 = x0.astype(int)
    y0 = y0.astype(int)
    
    x1 = x1.astype(int)
    y1 = y1.astype(int)
    
    intermediate_frame0 = old_frame
    intermediate_frame1 = old_frame

    for i in range(h):
            for j in range(w):
                if(valid_p(i+x0[i,j], j+y0[i,j], h, w)):
                    intermediate_frame0[i,j] = new_frame[i+x0[i,j],j+y0[i,j]]
                if(valid_p(i+x1[i,j], j+y1[i,j], h, w)):
                    intermediate_frame1[i,j] = new_frame[i+x1[i,j],j+y1[i,j]]
    
    out.writeFrame(intermediate_frame0)
    out.writeFrame(intermediate_frame1)
    out.writeFrame(new_frame)
    origin.writeFrame(new_frame)
    old_frame = new_frame
    




#for cont in range(0,10):
#    print(cont)
#    #Capturing the new frame
#    ret, new_frame = cap.read()
#    new_frame = cv2.cvtColor(new_frame,cv2.COLOR_BGR2GRAY)
#    flow = cv2.calcOpticalFlowFarneback(old_frame,new_frame, None, 0.5, 3, 15, 3, 5, 1.2, 0)
#    x = flow[...,0]
#    y = flow[...,1]
#    mag, ang = cv2.cartToPolar(flow[...,0], flow[...,1],angleInDegrees=True)
#    
#    #angulo = ang*180/np.pi
#    angulo = ang
#    mag0 = 1*mag/3
#    mag1 = mag/2
#
#    mag = mag.astype(int)
#    mag0 = mag0.astype(int)
#    mag1 = mag1.astype(int)
#    x = x.astype(int)
#    y = y.astype(int)
#    #intermediate_frame0 = old_frame
#    intermediate_frame1 = old_frame
#
#    for i in range(h):
#            for j in range(w):
#                if(mag1[i,j] != 0):
#                    if(angulo[i,j] >= 0 and angulo[i,j] <= 22.5) or (angulo[i,j] > 337.5 and angulo[i,j] <= 360):
#                        if(valid_p(i, j+mag1[i,j], h, w)):
#                            #intermediate_frame0[i, j+mag0[i,j]] = old_frame[i, j]
#                            intermediate_frame1[i, j+mag1[i,j]] = old_frame[i, j] 
#                            
#                    elif(angulo[i,j] > 22.5 and angulo[i,j] <= 67.5):
#                        if(valid_p(i-mag1[i,j], j + mag1[i,j], h, w)):
#                            #intermediate_frame0[i-mag0[i,j], j+mag0[i,j]] = old_frame[i, j]
#                            intermediate_frame1[i-mag1[i,j], j+mag1[i,j]] = old_frame[i, j] 
#                            
#                    elif(angulo[i,j] > 67.5 and angulo[i,j] <= 112.5):
#                        if(valid_p(i-mag1[i,j], j, h, w)):
#                            #intermediate_frame0[i-mag0[i,j], j] = old_frame[i, j]
#                            intermediate_frame1[i-mag1[i,j], j] = old_frame[i, j]
#                            
#                    elif(angulo[i,j] > 112.5 and angulo[i,j] <= 157.5):
#                        if(valid_p(i-mag1[i,j], j-mag1[i,j], h, w)):
#                           #intermediate_frame0[i-mag0[i,j], j-mag0[i,j]] = old_frame[i, j]
#                           intermediate_frame1[i-mag1[i,j], j-mag1[i,j]] = old_frame[i, j]
#                   
#                    elif(angulo[i,j] > 157.5 and angulo[i,j] <= 202.5):
#                        if(valid_p(i, j-mag1[i,j], h, w)):
#                           #intermediate_frame0[i, j-mag0[i,j]] = old_frame[i, j]
#                           intermediate_frame1[i, j-mag1[i,j]] = old_frame[i, j]
#                    
#                    elif(angulo[i,j] > 202.5 and angulo[i,j] <= 247.5):
#                        if(valid_p(i+mag1[i,j], j-mag1[i,j], h, w)):
#                           #intermediate_frame0[i+mag0[i,j], j-mag0[i,j]] = old_frame[i, j]
#                           intermediate_frame1[i+mag1[i,j], j-mag1[i,j]] = old_frame[i, j]
#                    
#                    elif(angulo[i,j] > 247.5 and angulo[i,j] <= 292.5):
#                        if(valid_p(i+mag1[i,j], j, h, w)):
#                           #intermediate_frame0[i+mag0[i,j], j] = old_frame[i, j]
#                           intermediate_frame1[i+mag1[i,j], j] = old_frame[i, j]
#                           
#                    elif(angulo[i,j] > 292.5 and angulo[i,j] <= 337.5):
#                        if(valid_p(i+mag1[i,j], j+mag1[i,j], h, w)):
#                           #intermediate_frame0[i+mag0[i,j], j+mag0[i,j]] = old_frame[i, j]
#                           intermediate_frame1[i+mag1[i,j], j+mag1[i,j]] = old_frame[i, j]
#                
#    #out.write(intermediate_frame0)
#    out.write(intermediate_frame1)
#    
#    out.write(new_frame)
#    out2.write(new_frame)
#    cont0+=1
#    cv2.imwrite("Real/"+str(cont0)+".png",new_frame)
#    #cont1+=1
#    #cv2.imwrite("Slow/"+str(cont1)+".png",intermediate_frame0)
#    cont1+=1
#    cv2.imwrite("Slow/"+str(cont1)+".png",intermediate_frame1)
#    cont1+=1
#    cv2.imwrite("Slow/"+str(cont1)+".png",new_frame)
#    new_frame = old_frame

cap.release()
out.close()
origin.close()

                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
