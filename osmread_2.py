import osmium as o
import sys
import shapely.wkb as wkblib
import pandas as pd
import numpy as np
import time

wkbfab = o.geom.WKBFactory()
output_file = open("building_data.csv","a")
class amenityListHandler(o.SimpleHandler):

    def print_amenity(amenity, tags, lon, lat):
        name = tags.get('name', '')
        print("%f %f %-15s %s" % (lon, lat, tags['amenity'], name))
        output_file.write(str(lon)+","+str(lat)+","+str(tags['amenity'])+","+str(name)+"\n")

    def node(self, n):
        if 'amenity' in n.tags:
            self.print_amenity(n.tags, n.location.lon, n.location.lat)

    def area(self, a):
        if 'amenity' in a.tags:
            wkb = wkbfab.create_multipolygon(a)
            poly = wkblib.loads(wkb, hex=True)
            centroid = poly.representative_point()
            self.print_amenity(a.tags, centroid.x, centroid.y)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python osmread_2.py <osmfile>")
        sys.exit(-1)

    handler = amenityListHandler()
    handler.apply_file(sys.argv[1])
execfile("compare_xy.py")