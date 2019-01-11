# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 09:35:40 2019

@author: jmat
"""

import folium

#Creating nap object with Coordinates
#map=folium.Map(location=[12.978249,77.664931])


#To Zoom from start at 20x
map=folium.Map(location=[12.978249,77.664931],zoom_start=20)
map.add_child(folium.Marker(location=[12.978249,77.664931] ,popup="Cypress Semiconductors", icon=folium.Icon(color="green")))
map.save("Banglore_withMarker.html")