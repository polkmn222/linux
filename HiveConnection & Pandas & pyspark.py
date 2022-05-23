#!/usr/bin/env python
# coding: utf-8

# In[ ]:


### Hive Database에 접근하는 외부 파이썬


# In[ ]:


from impala.dbapi import connect

conn = connect(host='192.168.66.128', port=10000, database="userdb", auth_mechanism='PLAIN')
cursor = conn.cursor()
cursor.execute('select * from employee')
# print(cursor.fetchall())

for row in cursor.fetchall():
    num, name, salary, destination = row
    print("{}\t{:12}\t{}\t{}\t ".format(num, name, salary, destination))


# In[1]:


import pandas as pd


# In[3]:


df = pd.DataFrame({'A':[2,4,8], 
                   'B':[5,8,2], 
                   'C':[9,5,7]})
print(df)


# In[5]:


print(df.sum())  #  세로


# In[6]:


print(df.sum(axis=1))  #  가로


# In[1]:


import findspark
findspark.init()

import pyspark              # only run after findspark.init()
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

df = spark.sql('''select 'spark' as hello ''')
df.show()

