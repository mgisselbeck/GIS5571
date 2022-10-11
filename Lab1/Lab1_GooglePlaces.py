from arcgis.gis import GIS
gis = GIS("home")

import requests

url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=44.976248%2C-93.229443&radius=15000&type=restaurant&keyword=restaurant&key=MY-API-KEY"

#Change location to Minneapolis

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

import pandas
import json
r_json=response.json()["results"]

df=pandas.DataFrame(columns=("Name", "Latitude","Longitude"))

for feature in range(len(r_json)):
    name=[r_json[feature]["name"]]
    Latitude=[r_json[feature]["geometry"]["location"]["lat"]]
    Longitude=[r_json[feature]["geometry"]["location"]["lng"]]
    
    df.loc[feature]=name+Latitude+Longitude
    
df.head()

import requests

url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=44.8988932%2C-93.4336059&radius=15000&type=restaurant&keyword=restaurant&key=AIzaSyBM8hTHQJ2WGdAYu92eTzfYA8kVSaGREAw"

#Change location to Minneapolis

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

import pandas
import json
r_json=response.json()["results"]

df=pandas.DataFrame(columns=("Name", "Latitude","Longitude"))

for feature in range(len(r_json)):
    name=[r_json[feature]["name"]]
    Latitude=[r_json[feature]["geometry"]["location"]["lat"]]
    Longitude=[r_json[feature]["geometry"]["location"]["lng"]]
    
    df.loc[feature]=name+Latitude+Longitude
    
df.head()

print(df)

import pandas
from pathlib import Path
filepath = Path(r'C:Users\gisse015\Documents\GIS5571\GooglePlaces.csv')
filepath.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(filepath)

arcpy.management.DefineProjection("GooglePlaces_1_2_XYTableToPoint", 'GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]')

display(df)

arcpy.conversion.TableToTable("GooglePlaces.csv", r"C:\Users\gisse015\Documents\ArcGIS\Projects\Lab1_2\Lab1_2.gdb", "GooglePlaces_1_2", '', 'Field1 "Field1" true true false 4 Long 0 0,First,#,GooglePlaces.csv,Field1,-1,-1;Name "Name" true true false 8000 Text 0 0,First,#,GooglePlaces.csv,Name,0,8000;Latitude "Latitude" true true false 8 Double 0 0,First,#,GooglePlaces.csv,Latitude,-1,-1;Longitude "Longitude" true true false 8 Double 0 0,First,#,GooglePlaces.csv,Longitude,-1,-1', '')

arcpy.conversion.FeatureClassToGeodatabase("GooglePlaces_1_2_XYTableToPoint", r"C:\Users\gisse015\Documents\ArcGIS\Projects\Lab1_2\Lab1_2.gdb")


