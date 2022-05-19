#!/usr/bin/python3

import sys

passengers = {'1958':[], '1959':[], '1960':[]}

for line in sys.stdin:
        line = line.strip()
        v, y = line.split('\t', 1)
        passengers[y.strip()].append( int(v.strip()))

avg = {}
avg['1958'] = sum( passengers['1958'])// len(passengers['1958'])
avg['1959'] = sum( passengers['1959'])// len(passengers['1959'])
avg['1960'] = sum( passengers['1960'])// len(passengers['1960'])

print(avg) 

# import pandas as pd
# import numpy as np
# from hdfs import InsecureClient
# # b = []
# try:
#     with open('airtravel.csv') as fin:
#         contents = fin.read()
#     # print(type(contents))
#     a = contents.split(',')
#     # print(type(a))
#     # print(len(a))
#     # print(a)
#     b = []
#     b0 = ""
#     b1 = []
#     b2 = []
# 
#     for i in range(1, len(a), 4):
#         c = a[i].strip()
#         #c = a[i].replace('"',"")
#         #c = a[i].replace("'","")
#         b0 = a[1].strip()
#         c = a[i][1:5]
#         c = c.strip()
#         b.append(c)
#     #	b.append(a[i].replace(" ", ""))
# 
#     # print(b)
#     sum = 0
#     for i in range(1, len(b)):
#         sum += int(b[i])
#     # print(sum)	
#     avg = int(sum / len(b) - 1)
#     print(b0+"year", avg)
# 
# #b.append(contents)
# # print(len(b))
# # print(b)
# # a = []
# 
# #for i in range(48):
# #	c = b.split()
# #	a.append(c)
# 
# #print(len(a))
# #print(a)
# # b = contents.split(",")
# # a = []
# #contents = list(contents)
# #for i in b:
# #for i in range(len(b)):
# #	c = b.split(",")
# #	a.append(c)
# #print(contents)
# #print(len(a))
# #print(type(a))
# #print(a)
# except:
#     continue
