# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 09:58:04 2019

@author: jmat
"""

map=folium.Map(location=[12.978249,77.664931],zoom_start=15)
for coordinates in [ [12.978249,77.664931],[12.978611,77.661111] ]:
    map.add_child(folium.Marker(location=coordinates ,popup="Place", icon=folium.Icon(color="green")))
## Can be used for marking with  CSV data of markers
map.save("Banglore_withMultipleMarker_withLists.html")