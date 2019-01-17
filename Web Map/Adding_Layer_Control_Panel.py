# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 10:11:30 2019

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

fgv=folium.FeatureGroup(name="US Volcano Map")
x=list(data["LAT"])
y=list(data["LON"])
z=list(data["NAME"])
e=list(data["ELEV"])
for lat,lon,name,elev in zip(x,y,z,e):
    fgv.add_child(folium.CircleMarker(location=[lat,lon] ,radius=6,popup =name+" Elev:"+str(elev)+ " meters" ,fill_color=color_producer(elev),color="grey",fill_opacity=0.7))


fgp=folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=(open("world.json","r",encoding="utf-8-sig")).read(),
             style_function=lambda x : {"fillColor":"green" if x['properties']['POP2005'] <10000000
                                        else "orange" if 10000000<= x['properties']['POP2005'] <=20000000
                                        else "red"
                                        }
             ) )



map.add_child(fgv)
map.add_child(fgp)
#Make sure below line after adding feature group
map.add_child(folium.LayerControl())


## Can be used for marking with  CSV data of markers
map.save("Adding_Layer_Control_Panel.html")