# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 14:31:54 2019

@author: jmat
"""


import cv2,time
first_frame=None
video=cv2.VideoCapture(0)
while True:
    check,frame= video.read()
    
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0)
    
    if  first_frame is None:
        first_frame=gray
        continue
    
    delta_frame=cv2.absdiff(first_frame,gray)
    thresh_delta=cv2.threshold(delta_frame,7,255,cv2.THRESH_BINARY)[1]
    
    
    #thresh_delta=cv2.dilate(thresh_delta,None,iterations=2)
    
    print(gray)
    print(delta_frame)
    cv2.imshow("Grey",gray)
    cv2.imshow("Delta",delta_frame)
    cv2.imshow("Threshold Frame",thresh_delta)
    

    #resize_image=cv2.resize(  frame,( int(frame.shape[1]/3), int(frame.shape[0]/3)  )  )
    #cv2.imshow("Capturing",resize_image)
    
    key=cv2.waitKey(1)
    if key==ord('q'):
        break
video.release()
cv2.destroyAllWindows()