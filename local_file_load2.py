#! /usr/bin/python3

import findspark
findspark.init()
from pyspark.sql import SparkSession

sparkSession = SparkSession.builder.appName("pyspark-hdfs2").getOrCreate()

# read.load()는 다양한 옵션을 설정할 수 있다
df2 = sparkSession.read.load('/home/hduser/employee.csv',
    format='csv', sep=',', inferSchema='true', header='true')
# df2 = df2.toDF('id', 'name', 'salary', 'job')

df2.show()
