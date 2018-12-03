# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 18:11:33 2018

@author: jmat
"""

import folium

#Creating nap object with Coordinates
#map=folium.Map(location=[12.978249,77.664931])


#To Zoom from start at 6x
map=folium.Map(location=[12.978249,77.664931],zoom_start=10)

map.save("Banglore.html")