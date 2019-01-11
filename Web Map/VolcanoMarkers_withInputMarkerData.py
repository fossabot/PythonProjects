# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 10:20:01 2019

@author: jmat
"""

import pandas
import folium

data= pandas.read_csv("Volcanoes_USA.txt")

map=folium.Map(location=[38.58,-99.09],zoom_start=4)

fg=folium.FeatureGroup(name="My Map")
x=list(data["LAT"])
y=list(data["LON"])
z=list(data["ELEV"])
for lat,lon,elev in zip(x,y,z):
    map.add_child(folium.Marker(location=[lat,lon] ,popup="Volcano", icon=folium.Icon(color="green")))
## Can be used for marking with  CSV data of markers
map.save("VolcanoMarkers_withInputMarkerData.html")