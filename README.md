# Damage Analysis for UNOSAT
This program uses .shp file of the building centroids in a city and compares the elevation values of the same using digital elevation model in order to carry out damage analysis of a city in an automated way.

## Introduction
The program can be used in order to accurately carry out automated damage assessment for all of the buildings in a particular region.
The program is also compatible with openstreetmap files from where it extracts the building data and compares them so as to get the number of damaged buildings. However, in openstreet maps, in some regions, the buildings are not mapped. Therefore, the number of buildings that are found in the .osm file is lesser compared to actual number of buildings. As a result, a .shp file has to be used which consists of all the coordinates of the building centroids that have been mapped for a city in order to find damage in all of them pre and post disaster.
In most of the cases, this can be done with the help of a company under contract which can provide .shp file and data related to centroid of each building in a city with the highest accuracy possible.

## Digital Elevation Models
The damage assessment is carried out based on the digital elevation model of the city before and after the disaster. Digital Elevation Model consists of a 3 dimensional map of the city based on two stereo image pairs which are combined together to get an idea about the elevation of the structures that are present in the city. This also provides us to carry out damage analysis in a very accurate way and get the actual damage for each of the buildings using their coordinates and comparing them with the coordinates in the DEM.
Other things that can be found out using this method is:
1) Number of buildings in the city
2) Development or increase in elevation of buildings in a city over time.
3) Percentage damage to each of the buildings in the city
4) Number of buildings that have been completely damaged

## Steps to Use
- Data related to a particular are of disaster is downloaded. This includes:
  1) Digital Elevation Model of the area (in .csv format), before and after the disaster.
  2) .shp file/.osm file for the buildings in the area that have been mapped and whose damage is to be found.
- Run `python osmread.py` in order to extract coordinates from .osm file or convert the custom .shp file to .csv format
- Make sure the files are named pre_disaster_data.csv and post_disaster_data.csv and building_data.csv after carrying out all the previous steps.
- Run `python compare_xy.py` and wait for the program to carry out the operation.
- The results are store in the .txt file that is generated and consists of the coordinate of the buildings, elevation change %age and damage significance.
### For faster processing, split the datasets into smaller sections and execute this program in parallel on them.
