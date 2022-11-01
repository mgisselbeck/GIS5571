import arcpy
import requests
import io
import zipfile
import pandas as pd
import os

proj_gdb = r'C:\Users\gisse015\Documents\ArcGIS\Projects\Lab1_1\Lab1_MNGeospatialCommons.gdb'
working_fold = r'C:\Users\gisse015\Documents\ArcGIS\Projects\Lab1_1'

arcpy.env.workspace = proj_gdb

arcpy.env.workspace

mn_geospatial_home = "https://resources.gisdata.mn.gov/pub/gdrs/data/"

rqst_objct = requests.get(mn_geospatial_home)
rqst_objct 

req_text = rqst_objct.text
req_text

pathto2016 = r'https://resources.gisdata.mn.gov/pub/gdrs/data/pub/us_mn_state_pca/env_assessed_water_2016/fgdb_env_assessed_water_2016.zip'

post_req_obj = requests.post(pathto2016)
post_req_obj.content

outputpath = r'C:\Users\gisse015\Documents\ArcGIS\Projects\Lab1_1'

pathto2016 = r'https://resources.gisdata.mn.gov/pub/gdrs/data/pub/us_mn_state_pca/env_assessed_water_2016/fgdb_env_assessed_water_2016.zip'

outputpath = r'C:\Users\gisse015\Documents\ArcGIS\Projects\Lab1_1'

post_req_obj = requests.post(pathto2016)
post_req_obj.content

post_req_obj.content

post_req_obj = requests.post(pathto2016)
post_req_obj.content

io.BytesIO(post_req_obj.content)

zipster = zipfile.ZipFile(io.BytesIO(post_req_obj.content))

zipster.extractall(outputpath)

pathto2022 = r'https://resources.gisdata.mn.gov/pub/gdrs/data/pub/us_mn_state_pca/env_assessed_water_2022/fgdb_env_assessed_water_2022.zip'

outputpath = r'C:\Users\gisse015\Documents\ArcGIS\Projects\Lab1_1.gdb'

post_req_obj = requests.post(pathto2022)

post_req_obj.content

post_req_obj = requests.post(pathto2022)
post_req_obj.content

io.BytesIO(post_req_obj.content)

zipster = zipfile.ZipFile(io.BytesIO(post_req_obj.content))

zipster.extractall(proj_gdb)

arcpy.conversion.FeatureClassToFeatureClass("assessed_2022_lakes_points", r"C:\Users\gisse015\Documents\ArcGIS\Projects\Lab1_1\Lab1_1.gdb", "Assessed_Lakes_2022", '', 'AUID "AUID" true true false 16 Text 0 0,First,#,assessed_2022_lakes_points,AUID,0,16;NAME "NAME" true true false 100 Text 0 0,First,#,assessed_2022_lakes_points,NAME,0,100;LOC_DESC "LOC_DESC" true true false 120 Text 0 0,First,#,assessed_2022_lakes_points,LOC_DESC,0,120;USE_CLASS "USE_CLASS" true true false 15 Text 0 0,First,#,assessed_2022_lakes_points,USE_CLASS,0,15;WATER_SIZE "WATER_SIZE" true true false 4 Float 0 0,First,#,assessed_2022_lakes_points,WATER_SIZE,-1,-1;AQR "AQR" true true false 4 Text 0 0,First,#,assessed_2022_lakes_points,AQR,0,4;AQR_CAT "AQR_CAT" true true false 4 Text 0 0,First,#,assessed_2022_lakes_points,AQR_CAT,0,4;AQR_LAST_AY "AQR_LAST_AY" true true false 4 Text 0 0,First,#,assessed_2022_lakes_points,AQR_LAST_AY,0,4;AQC "AQC" true true false 4 Text 0 0,First,#,assessed_2022_lakes_points,AQC,0,4;AQC_CAT "AQC_CAT" true true false 4 Text 0 0,First,#,assessed_2022_lakes_points,AQC_CAT,0,4;AQC_LAST_AY "AQC_LAST_AY" true true false 4 Text 0 0,First,#,assessed_2022_lakes_points,AQC_LAST_AY,0,4;AQL "AQL" true true false 4 Text 0 0,First,#,assessed_2022_lakes_points,AQL,0,4;AQL_CAT "AQL_CAT" true true false 4 Text 0 0,First,#,assessed_2022_lakes_points,AQL_CAT,0,4;AQL_LAST_AY "AQL_LAST_AY" true true false 4 Text 0 0,First,#,assessed_2022_lakes_points,AQL_LAST_AY,0,4;WR "WR" true true false 4 Text 0 0,First,#,assessed_2022_lakes_points,WR,0,4;WR_CAT "WR_CAT" true true false 4 Text 0 0,First,#,assessed_2022_lakes_points,WR_CAT,0,4;WR_LAST_AY "WR_LAST_AY" true true false 4 Text 0 0,First,#,assessed_2022_lakes_points,WR_LAST_AY,0,4;DW "DW" true true false 4 Text 0 0,First,#,assessed_2022_lakes_points,DW,0,4;DW_CAT "DW_CAT" true true false 4 Text 0 0,First,#,assessed_2022_lakes_points,DW_CAT,0,4;DW_LAST_AY "DW_LAST_AY" true true false 4 Text 0 0,First,#,assessed_2022_lakes_points,DW_LAST_AY,0,4;HUC_8 "HUC_8" true true false 8 Text 0 0,First,#,assessed_2022_lakes_points,HUC_8,0,8', '')

arcpy.conversion.FeatureClassToFeatureClass("assessed_2016_lakes_points", r"C:\Users\gisse015\Documents\ArcGIS\Projects\Lab1_1\Lab1_1.gdb", "Assessed_Lakes_2016", '', 'AUID "AUID" true true false 16 Text 0 0,First,#,assessed_2016_lakes_points,AUID,0,16;NAME "NAME" true true false 100 Text 0 0,First,#,assessed_2016_lakes_points,NAME,0,100;LOC_DESC "LOC_DESC" true true false 120 Text 0 0,First,#,assessed_2016_lakes_points,LOC_DESC,0,120;USE_CLASS "USE_CLASS" true true false 15 Text 0 0,First,#,assessed_2016_lakes_points,USE_CLASS,0,15;WATER_SIZE "WATER_SIZE" true true false 4 Float 0 0,First,#,assessed_2016_lakes_points,WATER_SIZE,-1,-1;AQR "AQR" true true false 4 Text 0 0,First,#,assessed_2016_lakes_points,AQR,0,4;AQR_CAT "AQR_CAT" true true false 4 Text 0 0,First,#,assessed_2016_lakes_points,AQR_CAT,0,4;AQR_LAST_AY "AQR_LAST_AY" true true false 4 Text 0 0,First,#,assessed_2016_lakes_points,AQR_LAST_AY,0,4;AQC "AQC" true true false 4 Text 0 0,First,#,assessed_2016_lakes_points,AQC,0,4;AQC_CAT "AQC_CAT" true true false 4 Text 0 0,First,#,assessed_2016_lakes_points,AQC_CAT,0,4;AQC_LAST_AY "AQC_LAST_AY" true true false 4 Text 0 0,First,#,assessed_2016_lakes_points,AQC_LAST_AY,0,4;AQL "AQL" true true false 4 Text 0 0,First,#,assessed_2016_lakes_points,AQL,0,4;AQL_CAT "AQL_CAT" true true false 4 Text 0 0,First,#,assessed_2016_lakes_points,AQL_CAT,0,4;AQL_LAST_AY "AQL_LAST_AY" true true false 4 Text 0 0,First,#,assessed_2016_lakes_points,AQL_LAST_AY,0,4;WR "WR" true true false 4 Text 0 0,First,#,assessed_2016_lakes_points,WR,0,4;WR_CAT "WR_CAT" true true false 4 Text 0 0,First,#,assessed_2016_lakes_points,WR_CAT,0,4;WR_LAST_AY "WR_LAST_AY" true true false 4 Text 0 0,First,#,assessed_2016_lakes_points,WR_LAST_AY,0,4;DW "DW" true true false 4 Text 0 0,First,#,assessed_2016_lakes_points,DW,0,4;DW_CAT "DW_CAT" true true false 4 Text 0 0,First,#,assessed_2016_lakes_points,DW_CAT,0,4;DW_LAST_AY "DW_LAST_AY" true true false 4 Text 0 0,First,#,assessed_2016_lakes_points,DW_LAST_AY,0,4;HUC_8 "HUC_8" true true false 8 Text 0 0,First,#,assessed_2016_lakes_points,HUC_8,0,8', '')


with arcpy.EnvManager(scratchWorkspace=r"C:\Users\gisse015\Documents\ArcGIS\Projects\Lab1_1\Lab1_1.gdb", workspace=r"C:\Users\gisse015\Documents\ArcGIS\Projects\Lab1_1\Lab1_1.gdb"):
    arcpy.analysis.SpatialJoin("Assessed_Lakes_2022", "Assessed_Lakes_2016", r"C:\Users\gisse015\Documents\ArcGIS\Projects\Lab1_1\Lab1_1.gdb\Assessed_Lakes_2016_2022", "JOIN_ONE_TO_MANY", "KEEP_ALL", 'AUID "AUID" true true false 16 Text 0 0,First,#,Assessed_Lakes_2022,AUID,0,16;NAME "NAME" true true false 100 Text 0 0,First,#,Assessed_Lakes_2022,NAME,0,100;LOC_DESC "LOC_DESC" true true false 120 Text 0 0,First,#,Assessed_Lakes_2022,LOC_DESC,0,120;USE_CLASS "USE_CLASS" true true false 15 Text 0 0,First,#,Assessed_Lakes_2022,USE_CLASS,0,15;WATER_SIZE "WATER_SIZE" true true false 4 Float 0 0,First,#,Assessed_Lakes_2022,WATER_SIZE,-1,-1;AQR "AQR" true true false 4 Text 0 0,First,#,Assessed_Lakes_2022,AQR,0,4;AQR_CAT "AQR_CAT" true true false 4 Text 0 0,First,#,Assessed_Lakes_2022,AQR_CAT,0,4;AQR_LAST_AY "AQR_LAST_AY" true true false 4 Text 0 0,First,#,Assessed_Lakes_2022,AQR_LAST_AY,0,4;AQC "AQC" true true false 4 Text 0 0,First,#,Assessed_Lakes_2022,AQC,0,4;AQC_CAT "AQC_CAT" true true false 4 Text 0 0,First,#,Assessed_Lakes_2022,AQC_CAT,0,4;AQC_LAST_AY "AQC_LAST_AY" true true false 4 Text 0 0,First,#,Assessed_Lakes_2022,AQC_LAST_AY,0,4;AQL "AQL" true true false 4 Text 0 0,First,#,Assessed_Lakes_2022,AQL,0,4;AQL_CAT "AQL_CAT" true true false 4 Text 0 0,First,#,Assessed_Lakes_2022,AQL_CAT,0,4;AQL_LAST_AY "AQL_LAST_AY" true true false 4 Text 0 0,First,#,Assessed_Lakes_2022,AQL_LAST_AY,0,4;WR "WR" true true false 4 Text 0 0,First,#,Assessed_Lakes_2022,WR,0,4;WR_CAT "WR_CAT" true true false 4 Text 0 0,First,#,Assessed_Lakes_2022,WR_CAT,0,4;WR_LAST_AY "WR_LAST_AY" true true false 4 Text 0 0,First,#,Assessed_Lakes_2022,WR_LAST_AY,0,4;DW "DW" true true false 4 Text 0 0,First,#,Assessed_Lakes_2022,DW,0,4;DW_CAT "DW_CAT" true true false 4 Text 0 0,First,#,Assessed_Lakes_2022,DW_CAT,0,4;DW_LAST_AY "DW_LAST_AY" true true false 4 Text 0 0,First,#,Assessed_Lakes_2022,DW_LAST_AY,0,4;HUC_8 "HUC_8" true true false 8 Text 0 0,First,#,Assessed_Lakes_2022,HUC_8,0,8;AUID_1 "AUID" true true false 16 Text 0 0,First,#,Assessed_Lakes_2016,AUID,0,16;NAME_1 "NAME" true true false 100 Text 0 0,First,#,Assessed_Lakes_2016,NAME,0,100;LOC_DESC_1 "LOC_DESC" true true false 120 Text 0 0,First,#,Assessed_Lakes_2016,LOC_DESC,0,120;USE_CLASS_1 "USE_CLASS" true true false 15 Text 0 0,First,#,Assessed_Lakes_2016,USE_CLASS,0,15;OVERALLCAT "OVERALLCAT" true true false 3 Text 0 0,First,#,Assessed_Lakes_2016,OVERALLCAT,0,3;CYCLE_LAST "CYCLE_LAST" true true false 4 Text 0 0,First,#,Assessed_Lakes_2016,CYCLE_LAST,0,4;WATER_SIZE_1 "WATER_SIZE" true true false 8 Double 0 0,First,#,Assessed_Lakes_2016,WATER_SIZE,-1,-1;AQR_1 "AQR" true true false 2 Text 0 0,First,#,Assessed_Lakes_2016,AQR,0,2;AQR_CAT_1 "AQR_CAT" true true false 2 Text 0 0,First,#,Assessed_Lakes_2016,AQR_CAT,0,2;AQC_1 "AQC" true true false 2 Text 0 0,First,#,Assessed_Lakes_2016,AQC,0,2;AQC_CAT_1 "AQC_CAT" true true false 2 Text 0 0,First,#,Assessed_Lakes_2016,AQC_CAT,0,2;AQL_1 "AQL" true true false 2 Text 0 0,First,#,Assessed_Lakes_2016,AQL,0,2;AQL_CAT_1 "AQL_CAT" true true false 2 Text 0 0,First,#,Assessed_Lakes_2016,AQL_CAT,0,2;DW_1 "DW" true true false 2 Text 0 0,First,#,Assessed_Lakes_2016,DW,0,2;DW_CAT_1 "DW_CAT" true true false 2 Text 0 0,First,#,Assessed_Lakes_2016,DW_CAT,0,2;ORIG_FID "ORIG_FID" true true false 4 Long 0 0,First,#,Assessed_Lakes_2016,ORIG_FID,-1,-1', "INTERSECT", None, '')

assessed_lakes_2016_2022 = r"C:\Users\gisse015\Documents\ArcGIS\Projects\Lab1_1\Lab1_1.gdb\Assessed_Lakes_2016_2022

arcpy.Describe(assessed_lakes_2016_2022).spatialReference

fields = ['NAME', 'LOC_DESC', 'USE_CLASS']

with arcpy.da.SearchCursor(assessed_lakes_2016, fields) as cursor:
    for row in cursor:
        if'Douglas' in row[1]:
            print(row)

df = pd.DataFrame([row for in arcpy.da.SearchCursor(assessed_lakes_2016_2022, fields)])
df.head

arcpy.conversion.FeatureClassToGeodatabase("Assessed_Lakes_2016_2022", r"C:\Users\gisse015\Documents\ArcGIS\Projects\Lab1_1\Lab1_1.gdb")

