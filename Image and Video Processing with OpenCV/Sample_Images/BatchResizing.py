# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 12:47:44 2019

@author: jmat
"""

import cv2
import glob

images=glob.glob("*.jpg")
#print(images)
for image in images:
    img=cv2.imread(image,0)
    re=cv2.resize(img,(100,100))
    cv2.imshow("Image",re)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_"+image,re)