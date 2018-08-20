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
i = 0
num = 0
decrease = {}

df = pd.read_csv("pre_disaster_aleppo_small.csv", error_bad_lines=False)
print (df.head())
print("Pre-Disaster Data Loaded Successfully!")
df2 = pd.read_csv("post_disaster_aleppo_small.csv", error_bad_lines=False)

print (df2.head())
print("Post-Disaster Data Loaded Successfully!")
df4 = pd.read_csv("building_data_small.csv",error_bad_lines=False)
print(df4.head())

output_file = open("results_"+ time.strftime("%Y%m%d%H%M%S")+".txt","a")
j = 0
l = 0

print("Processing")
for j in range (0,df4.shape[0]):
    for l in range (0,df.shape[0]):
        if ((df.iloc[l,0] == df4.iloc[j,0]) and (df.iloc[l,1] == df4.iloc[j,1])): 
            print("Match Found")
            for i in range(0,df.shape[0]):
                if ((df.iloc[l,0] == df4.iloc[j,0]) and (df.iloc[l,1] == df4.iloc[j,1]) and (df.iloc[l,0]==df2.iloc[i,0]) and  (df.iloc[l,1] == df2.iloc[i,1])):
                    print("Finding Elevation Change")
                    decrease[i] = ((df.iloc[i,2] - df2.iloc[i,2])*100)/(df.iloc[i,2])
                    if decrease[i] <5:
                        output_file.write("Latitude: " + (str(df.iloc[i,0])) +" Longitude: " + (str(df.iloc[i,1])) + " Damage %age: "+(str(decrease[i])+" No Significant Change "+"\n"))
                        num = num+1
                    else:
                        output_file.write("Latitude: " + (str(df.iloc[i,0])) +" Longitude: " + (str(df.iloc[i,1])) + " Damage %age: "+(str(decrease[i])+" Damage Detected! "+"\n"))
                    break       
print("Process Finished!")
print("Number of Damaged Buildings: "+ str(num))