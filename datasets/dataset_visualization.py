import pandas as pd

df1 = pd.read_parquet("yellow_tripdata_2025-01.parquet", engine="pyarrow")
df2 = pd.read_parquet("yellow_tripdata_2025-02.parquet", engine="pyarrow")
df3 = pd.read_parquet("green_tripdata_2025-01.parquet", engine="pyarrow")
df4 = pd.read_parquet("green_tripdata_2025-02.parquet", engine="pyarrow")

# print(df1.head())
# print(df2.head())
# print(df3.head())
# print(df4.head())

print(df1.shape[0])
print(df2.shape[0])
print(df3.shape[0])
print(df4.shape[0])

# from pyspark.sql import SparkSession

# spark = SparkSession.builder.appName("ParquetExample").getOrCreate()
# df = spark.read.parquet("path/to/file.parquet")
# df.show()
