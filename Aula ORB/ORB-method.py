import cv2
import numpy as np

img = cv2.imread("Louvre.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

print(cv2.__version__)

#Criando o Descritor ORB
orb = cv2.ORB_create(100)

#Obtendo os keypoints por ORB
keypointsorb = orb.detect(gray,None)

print(len(keypointsorb))

image = cv2.drawKeypoints(img,keypointsorb, None, flags = cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow("Louvre com ORB",image)

cv2.waitKey(0)