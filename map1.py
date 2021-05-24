#imports
import folium
import pandas


#getting and formatting data
data = pandas.read_csv("Volcanoes.txt")
lon = list(data["LON"])
lat = list(data["LAT"])
elev = list(data["ELEV"])
name = list(data["NAME"])

def elevColour(elev):
    if el < 1000:
        return "green"
    elif el > 1000 and el < 2000:
        return "orange"
    else:
        return "red"
#initialize objects
map = folium.Map(location=[38.58,-99.09],zoom_start=6,tiles='Stamen Terrain')
fg = folium.FeatureGroup(name="My Map")

#Add volcano markers to feature group and then to map
for lt, ln, el, nm in zip(lat,lon, elev,name):
    fg.add_child(folium.Marker(location=[lt,ln],popup= nm + "\n elevation:" + str(el) + " m", icon=folium.Icon(color=elevColour(el))))

map.add_child(fg)

#create html map file
map.save("Map1.html")
