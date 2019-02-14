# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 17:04:34 2019

@author: jmat
"""
import os
import cv2,time

video=cv2.VideoCapture(0)
#a=1
while True:
#    a=a+1
    check,frame= video.read()
    
    
#    print(check)
#    print(frame)
    
    
    #gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    resize_image=cv2.resize(  frame,( int(frame.shape[1]/5), int(frame.shape[0]/5)  )  )
    #cv2.namedWindow("window",0)
    #cv2.moveWindow("window",100,100)
    cv2.imshow("window",resize_image)
    
    #os.system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "python" to true' ''') # To make window active
    key=cv2.waitKey(1)
    if key==ord('q'):
        break
#print(a,"Frames were captured")
video.release()
cv2.destroyAllWindows()