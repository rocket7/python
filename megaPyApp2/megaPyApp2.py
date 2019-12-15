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


def elev_color(elev):
    if elev >= 3000:
        return "darkred"
    elif elev >= 1500 and elev < 3000:
        return "red"
    else:
        return "lightred"

#help(folium.Map)
#Boston = latitude=42.36, longitude=-71.05)
# loc is index name based , iloc is index # based
def create_map(mapfile, markerfile):
    latitude = 40.36
    longitude = -91.05
    map = folium.Map(location=[latitude,longitude],zoom_start=6)
    #map = folium.Map(location=[45,-71],zoom_start=6,tiles="Mapbox Bright")
    #map.add_child(folium.Marker(location=[45,-72], popup="loc1", icon=(folium.Icon(color="red"))))

    volcanos = folium.FeatureGroup(name="Volcano's")
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

    html = """<h4>Volcano Information: </h4>
    Name: %s
    Elevation: %s m"""

    for i in volcano_list:
        iframe = folium.IFrame(html=html % (i[0],i[1]), width=200, height=100)
        volcanos.add_child(folium.CircleMarker(location=(i[2],i[3]),popup=folium.Popup(iframe),radius=10,icon=(folium.Icon(color=elev_color(i[1]))),fill_color=elev_color(i[1]), color='grey',opacity=0.7,tooltip=f"Name: {str(i[0])}"))
        #fg.add_child(folium.Marker(location=[i[2],i[3]],popup=folium.Popup(iframe),icon=  (folium.Icon(color=elev_color(i[1]))),tooltip=f"Name: {str(i[0])}"))
        #fg.add_child(folium.Marker(location=[i[2],i[3]],popup=f"Elevation: {str(i[1])}",icon=(folium.Icon(color=elev_color(i[1]))),tooltip=f"Name: {str(i[0])}"))
        #map.add_child(folium.Marker(location=[i[2],i[3]],popup=str(i[0]),icon=(folium.Icon(color="green")),tooltip=(i[1])))


    #folium.Marker([45.3288, -121.6625], popup='<i>Mt. Hood Meadows</i>', tooltip=tooltip).add_to(m)
    #map.add_child(folium.Choropleth(location=[46,-71], popup="loc1", icon=(folium.Icon(color="blue"))))
    #map.add_child(folium.CircleMarker(   popup="loc1", icon=(folium.Icon(color="red"))))
    #map.add_child(folium.Circle(radius=10, popup="loc1", icon=(folium.Icon(color="green"))))

    fg_overlay = folium.FeatureGroup("GeoJson Overlay")

    fg_overlay.add_child(folium.GeoJson(data=(open("world.json", "r", encoding="utf-8-sig").read()),style_function=lambda x: {"fillColor":"green" if x["properties"]["POP2005"] < 10000000 else "yellow" if 10000000 <= x["properties"]["POP2005"] < 20000000 else "red"}))


    map.add_child(volcanos)
    map.add_child(fg_overlay)
    map.save(mapfile)


if __name__ == '__main__':
    create_map("test.html","Volcanoes.txt")
