import folium
import pandas as pd

def map_creator(df, crime_type, save_name):
    map3 = folium.Map(location=Chi_Coordinates, zoom_start=12)
    for x in df[df.primary_type==crime_type].iterrows():
        lat = x[1][12]
        lon = x[1][15]
        folium.CircleMarker(location = [lat, lon], popup=x[1][0], radius = 2).add_to(map3)
    map3.save(outfile= save_name)