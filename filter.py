import csv
import pandas as pd
from pandas import DataFrame
import datetime
import numpy as np
import io
import os
import subprocess
import time

infile = "unfiltered_results.txt"
outfile = "inter_1.txt"

delete_list = ["Name: elav, dtype: float64"]
fin = open(infile)
fout = open(outfile, "w+")
for line in fin:
    for word in delete_list:
        line = line.replace(word, ",")
    fout.write(line)
fin.close()
fout.close()

infile = "inter_1.txt"
outfile = "inter_2.txt"

delete_list = [", ", ",  ", "   ", "  "]
fin = open(infile)
fout = open(outfile, "w+")
for line in fin:
    for word in delete_list:
        line = line.replace(word, ",")
    fout.write(line)
fin.close()
fout.close()

infile = "inter_2.txt"
outfile = "inter_3.txt"

delete_list = [",\n"," "]
fin = open(infile)
fout = open(outfile, "w+")
for line in fin:
    for word in delete_list:
        line = line.replace(word, "")
    fout.write(line)
fin.close()
fout.close()

os.remove("inter_1.txt")
os.remove("inter_2.txt")

results = pd.read_csv("inter_3.txt", error_bad_lines=False, names=['x', 'y','meta', 'elav'])
results.to_csv('elav_result.csv')
os.remove("inter_3.txt")