import arcpy

import requests
import datetime
import numpy as np
import pandas as pd
import os

import pandas as pd

df = pd.read_csv (r'C:\Users\gisse015\Documents\ArcGIS\Projects\Lab1\ndawn_1.csv')   #read the csv file (put 'r' before the path string to address any special characters in the path, such as '\'). Don't forget to put the file name at the end of the path + ".csv"
print (df)

import pandas as pd

df = pd.read_csv (r'C:\Users\gisse015\Documents\ArcGIS\Projects\Lab1\ndawnnew.csv')
print (df)

base_ndawn_url = "https://ndawn.ndsu.nodak.edu/table.csv"

master_params = {"station" : "110","variable" : "mdavt", "dfn" : "","year" : "2021","ttype" : "monthly", "quick_pick" : "", "begin_date" : "2020-02","count" : "122"}

req_response = requests.get(base_ndawn_url, params = master_params)

with open("ndawnnew.csv", "w") as newCSV_txt:
    newCSV_txt.write(req_response.content.decode('utf-8'))

peek = pd.read_csv('ndawnnew.csv', skiprows = 3)
peek.head()

import pandas as pd

base_ndawn_url = "https://ndawn.ndsu.nodak.edu/table.csv"

master_params = {"station" : "110","variable" : "mdavt", "dfn" : "","year" : "2019","ttype" : "monthly", "quick_pick" : "", "begin_date" : "2019-02","count" : "122"}

req_response = requests.get(base_ndawn_url, params = master_params)

with open("ndawnnew3.csv", "w") as newCSV_txt:
    newCSV_txt.write(req_response.content.decode('utf-8'))

peek = pd.read_csv('ndawnnew2.csv', skiprows = 3)
peek.head()=[]

import pandas as pd

df = pd.read_csv (r'C:\Users\gisse015\Documents\ArcGIS\Projects\Lab1\ndawnnew.csv', sep ='you_delimiter', header=None, engine='python')
print (df)

arcpy.conversion.TableToTable(r"C:\Users\gisse015\Documents\ArcGIS\Projects\Lab1\ndawnnew.csv", r"C:\Users\gisse015\Documents\ArcGIS\Projects\Lab1\Lab1.gdb", "ndawn_1", '', r'Station Name "Station Name" true true false 8000 Text 0 0,First,#,C:\Users\gisse015\Documents\ArcGIS\Projects\Lab1\ndawnnew.csv,Station Name,0,8000;Latitude "Latitude" true true false 8 Double 0 0,First,#,C:\Users\gisse015\Documents\ArcGIS\Projects\Lab1\ndawnnew.csv,Latitude,-1,-1;Longitude "Longitude" true true false 8 Double 0 0,First,#,C:\Users\gisse015\Documents\ArcGIS\Projects\Lab1\ndawnnew.csv,Longitude,-1,-1;Elevation "Elevation" true true false 4 Long 0 0,First,#,C:\Users\gisse015\Documents\ArcGIS\Projects\Lab1\ndawnnew.csv,Elevation,-1,-1;Year "Year" true true false 4 Long 0 0,First,#,C:\Users\gisse015\Documents\ArcGIS\Projects\Lab1\ndawnnew.csv,Year,-1,-1;Month "Month" true true false 4 Long 0 0,First,#,C:\Users\gisse015\Documents\ArcGIS\Projects\Lab1\ndawnnew.csv,Month,-1,-1;Avg Temp "Avg Temp" true true false 8 Double 0 0,First,#,C:\Users\gisse015\Documents\ArcGIS\Projects\Lab1\ndawnnew.csv,Avg Temp,-1,-1;Number Missing "Number Missing" true true false 4 Long 0 0,First,#,C:\Users\gisse015\Documents\ArcGIS\Projects\Lab1\ndawnnew.csv,Number Missing,-1,-1,C:\Users\gisse015\Documents\ArcGIS\Projects\Lab1\ndawnnew.csv,Number Missing,-1,-1;Number Estimated "Number Estimated" true true false 4 Long 0 0,First,#,C:\Users\gisse015\Documents\ArcGIS\Projects\Lab1\ndawnnew.csv,Number Estimated,-1,-1,C:\Users\gisse015\Documents\ArcGIS\Projects\Lab1\ndawnnew.csv,Number Estimated,-1,-1;Monthly Normal Average Air Temperature "Monthly Normal Average Air Temperature" true true false 8 Double 0 0,First,#,C:\Users\gisse015\Documents\ArcGIS\Projects\Lab1\ndawnnew.csv,Monthly Normal Average Air Temperature,-1,-1;Departure from Normal Monthly Average Air Temperature "Departure from Normal Monthly Average Air Temperature" true true false 8 Double 0 0,First,#,C:\Users\gisse015\Documents\ArcGIS\Projects\Lab1\ndawnnew.csv,Departure from Normal Monthly Average Air Temperature,-1,-1', '')

arcpy.conversion.TableToTable(r"C:\Users\gisse015\Documents\ArcGIS\Projects\Lab1\ndawnnew2.csv", r"C:\Users\gisse015\Documents\ArcGIS\Projects\Lab1\Lab1.gdb", "ndawn_2", '', r'Station Name "Station Name" true true false 8000 Text 0 0,First,#,C:\Users\gisse015\Documents\ArcGIS\Projects\Lab1\ndawnnew2.csv,Station Name,0,8000;LAT "LAT" true true false 8 Double 0 0,First,#,C:\Users\gisse015\Documents\ArcGIS\Projects\Lab1\ndawnnew2.csv,LAT,-1,-1;LONG "LONG" true true false 8 Double 0 0,First,#,C:\Users\gisse015\Documents\ArcGIS\Projects\Lab1\ndawnnew2.csv,LONG,-1,-1;Elevation "Elevation" true true false 4 Long 0 0,First,#,C:\Users\gisse015\Documents\ArcGIS\Projects\Lab1\ndawnnew2.csv,Elevation,-1,-1;Year "Year" true true false 4 Long 0 0,First,#,C:\Users\gisse015\Documents\ArcGIS\Projects\Lab1\ndawnnew2.csv,Year,-1,-1;Month "Month" true true false 4 Long 0 0,First,#,C:\Users\gisse015\Documents\ArcGIS\Projects\Lab1\ndawnnew2.csv,Month,-1,-1;Avg Temp "Avg Temp" true true false 8 Double 0 0,First,#,C:\Users\gisse015\Documents\ArcGIS\Projects\Lab1\ndawnnew2.csv,Avg Temp,-1,-1;Number Missing "Number Missing" true true false 4 Long 0 0,First,#,C:\Users\gisse015\Documents\ArcGIS\Projects\Lab1\ndawnnew2.csv,Number Missing,-1,-1,C:\Users\gisse015\Documents\ArcGIS\Projects\Lab1\ndawnnew2.csv,Number Missing,-1,-1;Number Estimated "Number Estimated" true true false 4 Long 0 0,First,#,C:\Users\gisse015\Documents\ArcGIS\Projects\Lab1\ndawnnew2.csv,Number Estimated,-1,-1,C:\Users\gisse015\Documents\ArcGIS\Projects\Lab1\ndawnnew2.csv,Number Estimated,-1,-1;Monthly Normal Average Air Temperature "Monthly Normal Average Air Temperature" true true false 8 Double 0 0,First,#,C:\Users\gisse015\Documents\ArcGIS\Projects\Lab1\ndawnnew2.csv,Monthly Normal Average Air Temperature,-1,-1;Departure from Normal Monthly Average Air Temperature "Departure from Normal Monthly Average Air Temperature" true true false 8 Double 0 0,First,#,C:\Users\gisse015\Documents\ArcGIS\Projects\Lab1\ndawnnew2.csv,Departure from Normal Monthly Average Air Temperature,-1,-1', '')

arcpy.management.XYTableToPoint("ndawn_1", r"C:\Users\gisse015\Documents\ArcGIS\Projects\Lab1\Lab1.gdb\ndawn_1_XYTableToPoint", "Longitude", "Latitude", None, 'GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119521E-09;0.001;0.001;IsHighPrecision')

arcpy.ba.FindNearbyLocations("ndawn_2_1", "Station", "ndawn_1_XYTableToPoint", r"C:\Users\gisse015\Documents\ArcGIS\Projects\Lab1\Lab1.gdb\ndawn_2_1_FindNearbyLocations", "STRAIGHT_LINE_DISTANCE", "MILES", 50, None, None, "DO_NOT_CREATE_REPORT", '', None, None, None, "TOWARD_STORES", None, "TIME_ZONE_AT_LOCATION", None)

with arcpy.EnvManager(scratchWorkspace=r"C:\Users\gisse015\Documents\ArcGIS\Projects\Lab1\Lab1.gdb", workspace=r"C:\Users\gisse015\Documents\ArcGIS\Projects\Lab1\Lab1.gdb"):
    arcpy.management.Merge("ndawn_1;ndawn_2", r"C:\Users\gisse015\Documents\ArcGIS\Projects\Lab1\Lab1.gdb\ndawn_1_Merge", 'Station "Name" true true false 4 Long 0 0,First,#,ndawn_1,Station,-1,-1,ndawn_2,Station,-1,-1;Latitude "Latitude" true true false 8 Double 0 0,First,#,ndawn_1,Latitude,-1,-1;Longitude "Longitude" true true false 8 Double 0 0,First,#,ndawn_1,Longitude,-1,-1;Elevation "Elevation" true true false 4 Long 0 0,First,#,ndawn_1,Elevation,-1,-1,ndawn_2,Elevation,-1,-1;Year "Year" true true false 4 Long 0 0,First,#,ndawn_1,Year,-1,-1,ndawn_2,Year,-1,-1;Month "Month" true true false 4 Long 0 0,First,#,ndawn_1,Month,-1,-1,ndawn_2,Month,-1,-1;Avg "Temp" true true false 4 Long 0 0,First,#,ndawn_1,Avg,-1,-1,ndawn_2,Avg,-1,-1;Number "Missing" true true false 4 Long 0 0,First,#,ndawn_1,Number,-1,-1,ndawn_2,Number,-1,-1;Number_1 "Estimated" true true false 4 Long 0 0,First,#,ndawn_1,Number_1,-1,-1,ndawn_2,Number_1,-1,-1;Monthly "Normal" true true false 4 Long 0 0,First,#,ndawn_1,Monthly,-1,-1,ndawn_2,Monthly,-1,-1;Departure "from" true true false 4 Long 0 0,First,#,ndawn_1,Departure,-1,-1,ndawn_2,Departure,-1,-1;LAT "LAT" true true false 8 Double 0 0,First,#,ndawn_2,LAT,-1,-1;LONG "LONG" true true false 8 Double 0 0,First,#,ndawn_2,LONG,-1,-1', "NO_SOURCE_INFO")


arcpy.management.XYTableToPoint("ndawn_1_Merge", r"C:\Users\gisse015\Documents\ArcGIS\Projects\Lab1\Lab1.gdb\ndawn_1_Merge_XYTableToPoint", "Longitude", "Latitude", None, 'GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119521E-09;0.001;0.001;IsHighPrecision')

arcpy.conversion.TableToGeodatabase("ndawn_1_Merge", r"C:\Users\gisse015\Documents\ArcGIS\Projects\Lab1\Lab1.gdb")

import pandas as pd

df = pd.read_csv(r'C:\Users\gisse015\Documents\ArcGIS\Projects\Lab1\ndawn_Join.csv')

df.head()


