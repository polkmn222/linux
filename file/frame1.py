import pandas as pd
import numpy as np
from hdfs import InsecureClient


data = {
	'A':[20, 14, 30],
	'B':[30, 45, 20]
}

df = pd.DataFrame(data)
print(df)

df2 = pd.read_csv('mydata.csv')
print(df2)

print(df2.describe())

with open('mydata.csv') as fin:
        contents = fin.read()


hdfs_client = InsecureClient('http://localhost:9870')
with hdfs_client.write('/user/sample.csv',overwrite=True, encoding='utf-8') as writer:
        writer.write(contents)
print('End of write')
