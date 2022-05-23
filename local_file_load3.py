#! /usr/bin/python3
import findspark
findspark.init()
from pyspark.sql import SparkSession

sparkSession = SparkSession.builder.appName("pyspark-hdfs1").getOrCreate()


# hdfs 영역으로부터 파일 읽어오기
df = sparkSession.read.csv('hdfs://localhost:9000/user/mydata/employee.csv')
df = df.toDF('id','name','salary','job') 
df.show()

df = df.withColumn('salary', df.salary+5000)
df.show()

df.write.csv('increase', mode='overwrite', header='true')
df = sparkSession.read.load('/home/hduser/pyspark/employee_increase.csv', format='csv', sep=',', inferSchema='true', header='true')  # csv 내의 헤더가 없는 경우
df.show()
