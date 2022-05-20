import pandas as pd
import numpy as np
from hdfs import InsecureClient

with open('names.dat') as fin:
	contents = fin.read()


hdfs_client = InsecureClient('http://localhost:9870')
with hdfs_client.write('/user/mydata/demo1.py',overwrite=True, encoding='utf-8') as writer:
	writer.write(contents)
print('End of write')
