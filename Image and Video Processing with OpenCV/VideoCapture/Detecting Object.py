# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 14:31:54 2019

@author: jmat
"""


import cv2,pandas
from datetime import datetime


first_frame=None
status_list=[0,0]
times=[]
df=pandas.DataFrame(columns=["Start","End"])

video=cv2.VideoCapture(0)

while True:
    check,frame= video.read()
    status=0
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0)
    
    if  first_frame is None:
        first_frame=gray
        continue
    
    delta_frame=cv2.absdiff(first_frame,gray)
    thresh_delta=cv2.threshold(delta_frame,20,255,cv2.THRESH_BINARY)[1]
<<<<<<< HEAD
=======
    
    
    thresh_delta=cv2.dilate(thresh_delta,None,iterations=5)
>>>>>>> master
    
    #print(gray)
    #print(delta_frame)
    
<<<<<<< HEAD
    thresh_delta=cv2.dilate(thresh_delta,None,iterations=5)
    
    #print(gray)
    #print(delta_frame)
    
    (cnts,_)=cv2.findContours(thresh_delta.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    
=======
    (cnts,_)=cv2.findContours(thresh_delta.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    
>>>>>>> master
    for contour in cnts:
        if cv2.contourArea(contour)< 10000:
            continue
        status=1
        (x,y,w,h)=cv2.boundingRect(contour)
        cv2.rectangle(frame,(x,y),(x+w,y+h), (0,255,0),3  )
<<<<<<< HEAD
    status_list.append(status)
    if status_list[-1]-status_list[-2]!=0:
        times.append(datetime.now())
=======
     
        
>>>>>>> master
        
    cv2.imshow("Grey",gray)
    cv2.imshow("Delta",delta_frame)
    cv2.imshow("Threshold Frame",thresh_delta)
    cv2.imshow("Color Frame",frame)
   
    #resize_image=cv2.resize(  frame,( int(frame.shape[1]/3), int(frame.shape[0]/3)  )  )
    #cv2.imshow("Capturing",resize_image)
    
    key=cv2.waitKey(1)
    if key==ord('q'):
        if status==1:
            times.append(datetime.now())
        break
<<<<<<< HEAD
#print(status_list)
#print(times)
for i in range(0,len(times),2):
    df=df.append( {"Start":times[i], "End":times[i+1]} ,ignore_index=True )
    
df.to_csv("MotionDetectedTimes.csv")
=======
    print(status)
    
>>>>>>> master
video.release()
cv2.destroyAllWindows()