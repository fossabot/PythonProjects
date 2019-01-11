# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 09:55:12 2019

@author: jmat
"""
import folium


map=folium.Map(location=[12.978249,77.664931],zoom_start=15)
map.add_child(folium.Marker(location=[12.978249,77.664931] ,popup="Cypress Semiconductors", icon=folium.Icon(color="green")))
map.add_child(folium.Marker(location=[12.978611,77.661111] ,popup="Random Place", icon=folium.Icon(color="red")))

map.save("Banglore_withMultipleMarker.html")