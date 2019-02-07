# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 09:54:46 2019

@author: jmat
"""

import cv2
bw_img=cv2.imread("166 galaxy.jpg",0  )   ##1  for rgb , 0 for  grayscale, -1 alpha image(transparency )

print(type(bw_img))
#print(bw_img)
print(bw_img.shape)
print(bw_img.ndim)


colour_img=cv2.imread("166 galaxy.jpg",1  )   ##1  for rgb , 0 for  grayscale, -1 alpha image(transparency )

print(type(colour_img))
#print(colour_img)
print(colour_img.shape)
print(colour_img.ndim)



#cv2.imshow("Galaxy",bw_img)
#cv2.waitKey(2000)
#cv2.destroyAllWindows()

#cv2.imshow("Galaxy",colour_img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


#resize_bw_image=cv2.resize(bw_img,(500,700))
#cv2.imshow("Galaxy",resize_bw_image)
#cv2.waitKey(2000)
#cv2.destroyAllWindows()

#resize_colour_image=cv2.resize(colour_img,(500,700))
#cv2.imshow("Galaxy",resize_colour_image)
#cv2.waitKey(2000)
#cv2.destroyAllWindows()




resize_bw_image=cv2.resize(  bw_img,( int(bw_img.shape[1]/2), int(bw_img.shape[0]/2)  )  )
print(resize_bw_image.shape)
cv2.imshow("Galaxy",resize_bw_image)
cv2.waitKey(2000)
cv2.destroyAllWindows()

resize_colour_image=cv2.resize (colour_img,( int(bw_img.shape[1]/2), int(bw_img.shape[0]/2)  )  )
print(resize_colour_image.shape)
cv2.imshow("Galaxy",resize_colour_image)
cv2.waitKey(2000)
cv2.destroyAllWindows()

cv2.imwrite("Galaxy_bw_Resixed.jpg",resize_bw_image)
cv2.imwrite("Galaxy_Colour_Resized.jpg",resize_colour_image)















