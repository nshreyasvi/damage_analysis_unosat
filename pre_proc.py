import csv
import pandas as pd
from pandas import DataFrame
import datetime
import numpy as np
import io
import os
import subprocess
import time

# Filtering the .asc file
# For Pre-Disaster Data

infile = "aleppo_2009.asc"
outfile = "inter_1.txt"

delete_list = ["  ", "   "]
fin = open(infile)
fout = open(outfile, "w+")
for line in fin:
    for word in delete_list:
        line = line.replace(word, " ")
    fout.write(line)
fin.close()
fout.close()

infile = "inter_1.txt"
outfile = "inter_2.txt"

delete_list = ["   ", "    "]
fin = open(infile)
fout = open(outfile, "w+")
for line in fin:
    for word in delete_list:
        line = line.replace(word, " ")
    fout.write(line)
fin.close()
fout.close()

infile = "inter_2.txt"
outfile = "inter_3.txt"

delete_list = ["  ", " "]
f1in = open(infile)
f1out = open(outfile, "w+")
for line in f1in:
    for word in delete_list:
        line = line.replace(word, ",")
    f1out.write(line)
f1in.close()
f1out.close()

os.remove("inter_1.txt")
os.remove("inter_2.txt")

n = 4
nfirstlines = []
with open("inter_3.txt") as f, open("aleppo_2009.csv", "w") as out:
    for x in xrange(n):
        nfirstlines.append(next(f))
    for line in f:
        line = line[1:]
        out.write(line)
os.remove("inter_3.txt")

#For Post Disaster Data:
infile = "aleppo_2014.asc"
outfile = "inter_1.txt"

delete_list = ["  ", "   "]
fin = open(infile)
fout = open(outfile, "w+")
for line in fin:
    for word in delete_list:
        line = line.replace(word, " ")
    fout.write(line)
fin.close()
fout.close()

infile = "inter_1.txt"
outfile = "inter_2.txt"

delete_list = ["   "]
fin = open(infile)
fout = open(outfile, "w+")
for line in fin:
    for word in delete_list:
        line = line.replace(word, " ")
    fout.write(line)
fin.close()
fout.close()

infile = "inter_2.txt"
outfile = "inter_3.txt"

delete_list = ["  ", " "]
f1in = open(infile)
f1out = open(outfile, "w+")
for line in f1in:
    for word in delete_list:
        line = line.replace(word, ",")
    f1out.write(line)
f1in.close()
f1out.close()

os.remove('inter_1.txt')
os.remove('inter_2.txt')

n = 4
nfirstlines = []
with open("inter_3.txt") as f, open("aleppo_2014.csv", "w") as out:
    for x in xrange(n):
        nfirstlines.append(next(f))
    for line in f:
        line = line[1:]
        out.write(line)
os.remove("inter_3.txt")

#Execute the other program
os.system('python fast_compare.py')