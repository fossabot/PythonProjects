# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 11:10:54 2019

@author: jmat
"""

import pandas
import folium

data= pandas.read_csv("Volcanoes_USA.txt")

def color_producer(elevation):
    if elevation <1000:
        return "green"
    elif 1000<= elevation <3000:
        return "orange"
    else:
        return "red"
    
map=folium.Map(location=[38.58,-99.09],zoom_start=6)

fg=folium.FeatureGroup(name="My Map")
x=list(data["LAT"])
y=list(data["LON"])
z=list(data["NAME"])
e=list(data["ELEV"])
for lat,lon,name,elev in zip(x,y,z,e):
    map.add_child(folium.CircleMarker(location=[lat,lon] ,radius=6,popup =name+" Elev:"+str(elev)+ " meters" ,fill_color=color_producer(elev),color="grey",fill_opacity=0.7))

## Can be used for marking with  CSV data of markers
map.save("Adding_and _Styling_Markers.html")