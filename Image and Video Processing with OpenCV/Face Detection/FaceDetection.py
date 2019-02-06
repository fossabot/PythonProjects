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
#print(faces)
#print(type(faces))


for x,y,w,h in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

resize_image=cv2.resize(  img,( int(img.shape[1]/3), int(img.shape[0]/3)  )  )

cv2.imshow("Image",resize_image)
cv2.waitKey(0)
cv2.destroyAllWindows()