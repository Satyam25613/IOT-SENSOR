import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from pyspark.sql.functions import col, to_timestamp, hour, dayofmonth, avg
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame

args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# 1. Read cleaned data from S3 (processed folder)
input_path = "s3://iot-sensor-data-satyam/processed/"
processed_dyf = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [input_path]},
    format="parquet"
)

# 2. Convert to Spark DataFrame
df = processed_dyf.toDF()

# 3. Extract hour and day
df = df.withColumn("hour", hour("timestamp"))
df = df.withColumn("day", dayofmonth("timestamp"))

# 4. Calculate hourly average temperature
hourly_avg = df.groupBy("day", "hour").agg(avg("temperature").alias("avg_temp"))

# 5. Convert back to DynamicFrame
dyf_hourly = DynamicFrame.fromDF(hourly_avg, glueContext, "dyf_hourly")

# 6. Write to aggregated folder
output_path = "s3://iot-sensor-data-satyam/aggregated/"
glueContext.write_dynamic_frame.from_options(
    frame=dyf_hourly,
    connection_type="s3",
    format="parquet",
    connection_options={"path": output_path}
)

job.commit()
