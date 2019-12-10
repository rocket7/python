'''
mega python course on udemy
application # 2

mapping program
'''

import os
import pandas
import folium
import shutil
import pandas
import numpy

#help(folium.Map)
#Boston = latitude=42.36, longitude=-71.05)
# loc is index name based , iloc is index # based
def create_map(mapfile, markerfile):
    latitude = 40.36
    longitude = -91.05
    map = folium.Map(location=[latitude,longitude],zoom_start=6)
    #map = folium.Map(location=[45,-71],zoom_start=6,tiles="Mapbox Bright")
    #map.add_child(folium.Marker(location=[45,-72], popup="loc1", icon=(folium.Icon(color="red"))))

    fg = folium.FeatureGroup(name="Adam Map")
    #os.chdir("megaPyApp2")
    fo=  open("Volcanoes.txt", "r")
    pdf = pandas.read_csv(fo)
    lat_long = pdf.iloc[1:,2:]

    #NEED TO ITERATE THROUGH COLUMN STRING VALUES TO LOAD LIST
    #volcano_list = list(lat_long["NAME"])
    volcano_list = [[]]

#first ..index is empty
    for n,e,la,lo in zip(list(lat_long["NAME"]),list(lat_long["ELEV"]),list(lat_long["LAT"]),list(lat_long["LON"])):
        volcano_list.append([n,e,la,lo])

        #volcano_list[i] = a,b,c - wrong need braces for list

    volcano_list.pop(0)

    #print(volcano_list)
    print(len(volcano_list))

    for i in volcano_list:
        fg.add_child(folium.Marker(location=[i[2],i[3]],popup=f"Elevation: {str(i[1])}",icon=(folium.Icon(color="green")),tooltip=f"Name: {str(i[0])}"))
        #map.add_child(folium.Marker(location=[i[2],i[3]],popup=str(i[0]),icon=(folium.Icon(color="green")),tooltip=(i[1])))


    #folium.Marker([45.3288, -121.6625], popup='<i>Mt. Hood Meadows</i>', tooltip=tooltip).add_to(m)
    #map.add_child(folium.Choropleth(location=[46,-71], popup="loc1", icon=(folium.Icon(color="blue"))))
    #map.add_child(folium.CircleMarker(   popup="loc1", icon=(folium.Icon(color="red"))))
    #map.add_child(folium.Circle(radius=10, popup="loc1", icon=(folium.Icon(color="green"))))
    map.add_child(fg)
    map.save(mapfile)


if __name__ == '__main__':
    create_map("test.html","Volcanoes.txt")
