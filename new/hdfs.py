#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
from hdfs import InsecureClient

client_hdfs = InsecureClient('http://192.168.66.128:9870')  # namenode의 웹 인터페이스
with client_hdfs.read('/user/sample.csv') as reader:
    df = pd.read_csv(reader,index_col=0)
print( df )

