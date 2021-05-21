#imports
import folium
import pandas

#getting and formatting data
data = pandas.read_csv("Volcanoes.txt")
lon = list(data["LON"])
lat = list(data["LAT"])
#initialize objects
map = folium.Map(location=[38.58,-99.09],zoom_start=6,tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="My Map")

#Add volcano markers to feature group and then to map
for lt, ln in zip(lat,lon):
    fg.add_child(folium.Marker(location=[lt,ln],popup="Hi I am a Marker", icon=folium.Icon(color='green')))
map.add_child(fg)

#create html map file
map.save("Map1.html")
