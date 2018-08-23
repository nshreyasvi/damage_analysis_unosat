# Damage Analysis using DEM data (UNOSAT)

**_Organization: UNOSAT (CERN Openlab 2018)
Supervisor: Lars Bromley
Student: Shreyasvi Natraj_**

## Introduction
The project revolves around finding the possibility to use elevation data related to a particular city before and after undergoing a specific type of disaster in order to be able to do a damage analysis for the area in an automated way.
Elevation data can be extracted from DEMs or Digital Elevation Models which are basically latitude, longitude and altitude data extracted from two satellite image stereo pairs for a particular city. This data in combination with building data extracted from shape file can be used to find out the number of damaged buildings in a particular city. A preliminary analysis can also be done based on openstreetmap building data in which depending upon the number of mapped buildings by openstreetmaps, the number of damaged buildings can be found.

## Steps to Use
This version consists of a openstreetmap scraper (in case building data is to be extracted from openstreetmaps models) and version which uses .csv files extracted from .shp file in order to do damage analysis for all the mapped buildings by comparing their elevation data before and after the event.

**Requirements**
`pip install numpy pandas csv time osmium`

The usage of the code can be done in several ways:

### Preparation of input data

**Building Data**
1) Usage with Openstreetmap:
- The building data for a particular city is first downloaded from openstreetmap.org in .osm format and kept in the same folder as the osmreader python programs.
- Run the command `python osmread.py <name of .osm file>` to extract all the building coordinate data as well as centroid for each of the buildings.
2) Usage with custom .shp file:
- Export the .shp file in .csv format using QGIS or any other external program

**Elevation Data**
- Elevation data is to be extracted from DEMs which are to be prepared from two image stereo pairs and exporting the raster in xyz file format.
- Elevation data (in xyz file format) can be automatically converted to the required .csv format by running `python pre_proc.py` program over the two DEM xyz files (*Right now for a 16 million coordinates file, it takes 7.5 minutes to process*)

Input file format follows the same format:
|     lat       |     long      |     elav      |
| ------------- | ------------- | ------------- |
| coordinate 1  | coordinate 1  |    elav 1     |
| coordinate 2  | coordinate 2  |    elav 2     |
| ------------- | ------------- | ------------- |

*In case of building data the third column would be replaced with metadata*
**NOTE: Coordinates of latitude and longitude for all the files have to be rounded up to 5th decimal point for consistent data**

## Running comparison program
- Run the command `python f_cmp_asc.py` or `python fast_compare.py` in order to run the algorithm over the dataset
- When the program is running, you will see cycle numbers, **cycle number will always equal to the number of buildings present in dataset*
- In order to run the program in background use `python f_cmp_asc.py > output.log &` or `python fast_compare.py > output.log &`.
- The status of the program can be found using the `top` or `output.log` file by simply opening it using notepad or any other text editor.
- The program must automatically run `filter.py` which is used to get data in an easy to understand format.
- The result file can also be imported to QGIS in order to see the damaged areas.

## Results:
*Results were tested for aleppo DEMs*

The elevation change is found in terms of percentage where
1) If elevation change percentage = -ve, it is increase in elevation at that coordinate point
2) If elevation change percentage = +ve, but less than the threshold value, it is usually change due to error in input data
3) If elevation change percentage = +ve, but has significant value such as >10, then there is damage to that particular building

**The value for threshold has to be set up be comparing these results with the ground truth i.e. pre analyzed areas which underwent damage**

## Future Work
The program requires a filter value to be set so as to remove elevation changes that are caused due to error in DEMs or input data. Upon finding the *sweet spot* for the filter value, a simple if statement can be used in order to remove all the noisy data and only take significant damage from this program.
