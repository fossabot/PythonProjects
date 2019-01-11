# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 10:26:01 2019

@author: jmat
"""

import pandas
import folium

data= pandas.read_csv("Volcanoes_USA.txt")

map=folium.Map(location=[38.58,-99.09],zoom_start=4)

fg=folium.FeatureGroup(name="My Map")
x=list(data["LAT"])
y=list(data["LON"])
z=list(data["NAME"])
e=list(data["ELEV"])
for lat,lon,name,elev in zip(x,y,z,e):
    if elev<1000:
        map.add_child(folium.Marker(location=[lat,lon] ,popup=str(name), icon=folium.Icon(color="green")))
    elif 1000<=elev <3000:
        map.add_child(folium.Marker(location=[lat,lon] ,popup=str(name), icon=folium.Icon(color="orange")))
    else:
        map.add_child(folium.Marker(location=[lat,lon] ,popup=str(name), icon=folium.Icon(color="red")))
## Can be used for marking with  CSV data of markers
map.save("VolcanoMarkers_withInputMarkerData_DynamicInfo_DynamicColour.html")