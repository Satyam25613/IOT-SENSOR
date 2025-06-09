IoT Sensor Data Processor
This project is designed to ingest, clean, transform, and aggregate raw IoT sensor data using AWS Glue and Amazon S3. It handles real-time sensor logs (temperature, humidity, etc.) and outputs cleaned and summarized datasets for further analysis or visualization.

Project Structure
S3 Buckets:
bash
Copy
Edit
s3://iot-sensor-data-satyam/
├── raw/         # Raw CSV sensor data
├── processed/   # Cleaned data stored in Parquet format
└── aggregated/  # Hourly average temperature in Parquet
Architecture Overview
Source: Raw IoT sensor logs (.csv) uploaded to raw/

ETL Job 1: Reads, cleans, transforms the data, stores results in processed/

ETL Job 2: Aggregates hourly average temperature, writes to aggregated/

ETL Steps
1. Cleaning & Transformation (ETL Job 1)
Reads CSV from raw/

Parses and converts timestamp

Filters out faulty temperature values (< -50 or > 150)

Writes output as Parquet to processed/

2. Aggregation (ETL Job 2)
Reads Parquet from processed/

Extracts hour and day from timestamp

Calculates average temperature grouped by hour

Writes aggregated data to aggregated/

Technologies Used
AWS Glue (ETL pipelines using Spark & PySpark)

Amazon S3 (Data storage: raw, processed, aggregated)

Apache Parquet (Efficient columnar storage format)

GitHub (Version control and documentation)

How to Run
Upload raw sensor logs (sensor-data.csv) to s3://iot-sensor-data-satyam/raw/

Trigger ETL Job 1 from AWS Glue to clean and transform the data

Trigger ETL Job 2 to generate hourly averages

Output will be available in the processed/ and aggregated/ S3 folders

Output Usage
You can:

Download Parquet files for analysis

Use AWS Athena to query data

Integrate with QuickSight or BI tools for visualization

