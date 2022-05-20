import pandas as pd
import numpy as np
from hdfs import InsecureClient

hdfs_client = InsecureClient('http://localhost:9870')
with hdfs_client.read('/user/sample.csv') as reader:
        df2 = pd.read_csv(reader, index_col=0)

print( df2.sum(axis=0) )  # axis 세로축
