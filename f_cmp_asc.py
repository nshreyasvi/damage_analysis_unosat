import csv
import pandas as pd
from pandas import DataFrame
import datetime
import numpy as np
import io
import os
import subprocess
import time

print("=================================================================\n This program determines decrease in elevation at different points in an area by checking latitude and longitude values of 2 digital elevation model xyz files")
num = 0

# Loading .csv files extracted from DEMs and .shp files
data_pre = pd.read_csv("aleppo_2009.csv", error_bad_lines=False, names=['lat', 'long', 'elav'])
data_pre.round({'lat': 5, 'long': 5})
print (data_pre.head())
print("Pre-Disaster Data Loaded Successfully!")

data_post = pd.read_csv("aleppo_2014.csv", error_bad_lines=False, names=['lat', 'long', 'elav'])
data_post.round({'lat': 5, 'long': 5})
print (data_post.head())
print("Post-Disaster Data Loaded Successfully!")

data_bld = pd.read_csv("building_data_small.csv",error_bad_lines=False)
data_bld.round(5)
print (data_bld.head())
print("Building Data Loaded Successfully")

# Defining Output File
output_file = open("unfiltered_results_asc.txt","a")

# Using .shp file for building counting and DEM for damage analysis
for index, bld in data_bld.iterrows():
    bld_long = bld[0]
    bld_lat = bld[1]

    bld_pre = data_pre.query('long == %s and lat == %s' % (bld_long, bld_lat))
    bld_post = data_post.query('long == %s and lat == %s' % (bld_long, bld_lat))

    if len(bld_pre) == 1 and len(bld_post):
        elav = ((bld_pre['elav'] - bld_post['elav']) / bld_pre['elav']) * 100
        text = (str(bld_lat)) + " " + (str(bld_long)) + " " + (str(elav))+"\n"
        num = num + 1
        output_file.write(text)
        print(text)
    print('Cycle: #%s' % index)

#Printing Details of the Process
print("Process finished with "+ num + "damaged buildings!\n")
print("Total number of buildings checked: "+ index+"\n")
#Execute the other program
os.system('python filter.py')