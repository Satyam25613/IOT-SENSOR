import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from pyspark.sql.functions import col, to_timestamp
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame

args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# 1. Read data from S3 (raw folder)
input_path = "s3://iot-sensor-data-satyam/raw/"
df = spark.read.csv(input_path, header=True, inferSchema=True)

# 2. Clean and transform
df_clean = df.withColumn("timestamp", to_timestamp("timestamp")) \
    .filter((col("temperature") > -50) & (col("temperature") < 150))

# 3. Convert to DynamicFrame
dyf_clean = DynamicFrame.fromDF(df_clean, glueContext, "dyf_clean")

# 4. Write cleaned data to processed/ in Parquet format
output_path = "s3://iot-sensor-data-satyam/processed/"
glueContext.write_dynamic_frame.from_options(
    frame=dyf_clean,
    connection_type="s3",
    format="parquet",
    connection_options={"path": output_path}
)

job.commit()
