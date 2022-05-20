import pandas as pd
import numpy as np
from hdfs import InsecureClient

client_hdfs = InsecureClient('http://localhost:9870')
with client_hdfs.read('/user/mydata/names.dat', encoding='utf-8') as reader:
	contents = reader.read()

print(contents)
