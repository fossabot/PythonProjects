# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 13:00:42 2019

@author: jmat
"""

import cv2

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img=cv2.imread("photo.jpg")

gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


faces=face_cascade.detectMultiScale(gray_img, scaleFactor=1.05,minNeighbors=5)
print(faces)
print(type(faces))

cv2.imshow("Image",gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()