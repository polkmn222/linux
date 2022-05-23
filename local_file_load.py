#! /usr/bin/python3
import findspark
findspark.init()
from pyspark.sql import SparkSession

sparkSession = SparkSession.builder.appName("pyspark-hdfs1").getOrCreate()


# 로컬에서 파일 로드
df1 = sparkSession.read.csv('/home/hduser/employee.csv')  # csv 내의 헤더가 없는 경우
df1 = df1.toDF('id','name','salary','job')        #  컬럼명 추가
df1.show()

# csv 파일에 헤더가 포함된 경우
#df2 = sparkSession.read.csv('emp_with_header.csv', header=True)
#df2.show()

# hdfs 영역으로부터 파일 읽어오기
df = sparkSession.read.csv('hdfs://localhost:9000/user/mydata/employee.csv')
df = df.toDF('id','name','salary','job') 
df.show()

df = df.withColumn('salary', df.salary+1000)
df.show()

