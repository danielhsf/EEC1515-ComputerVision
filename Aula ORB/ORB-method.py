import cv2
import numpy as np

img = cv2.imread("Louvre.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Criando o Descritor ORB
orb = cv2.ORB_create(100000)
fast = cv2.FastFeatureDetector_create(threshold = 20,nonmaxSuppression = 0,type = cv2.FAST_FEATURE_DETECTOR_TYPE_9_16)
#Obtendo os keypoints por ORB
keypointsorb = orb.detect(gray,None)
keypointsfast = fast.detect(gray,None)

#Obtendo os keypoints por FAST
print(len(keypointsorb))
print(len(keypointsfast))

image = cv2.drawKeypoints(img,keypointsorb, None, flags = cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow("Louvre com ORB",image)

cv2.waitKey(0)