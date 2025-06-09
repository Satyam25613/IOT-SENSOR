# IoT Sensor Data Processor

This project demonstrates an end-to-end ETL pipeline using AWS Glue and Amazon S3 to process IoT sensor data. It ingests raw sensor logs, performs data cleaning and transformation, calculates hourly temperature averages, and stores the outputs in an optimized format for analysis.

## S3 Bucket Structure

s3://iot-sensor-data-satyam/
├── raw/ # Raw CSV or JSON sensor data
├── processed/ # Cleaned and transformed data in Parquet format
└── aggregated/ # Hourly average temperature data in Parquet format

markdown
Copy
Edit

## Workflow Overview

1. **Raw Data Ingestion**
   - Sensor logs (e.g., temperature, humidity) are uploaded to the `raw/` folder in CSV format.

2. **ETL Job 1: Data Cleaning and Transformation**
   - Converts timestamps to proper format.
   - Filters out temperature readings below -50°C or above 150°C.
   - Outputs the cleaned data to the `processed/` folder in Parquet format.

3. **ETL Job 2: Aggregation**
   - Reads cleaned data from the `processed/` folder.
   - Extracts the hour and day from the timestamp.
   - Calculates average temperature per hour.
   - Outputs the aggregated results to the `aggregated/` folder.

## Technologies Used

- **AWS Glue** – Serverless ETL engine using PySpark
- **Amazon S3** – Scalable object storage for data lake architecture
- **Apache Parquet** – Columnar data format for efficient querying
- **PySpark** – Distributed data processing
- **GitHub** – Version control and documentation

## How to Use

1. **Upload Raw Data**
   - Place your sensor CSV files into `s3://iot-sensor-data-satyam/raw/`

2. **Run ETL Jobs**
   - Execute **ETL Job 1** in AWS Glue to clean and store data in `processed/`
   - Execute **ETL Job 2** to compute hourly temperature averages into `aggregated/`

3. **Download or Query Results**
   - Use AWS Athena, QuickSight, or download Parquet files from `processed/` and `aggregated/` for analysis.

## Example Output

The aggregated output contains columns such as:

| day | hour | avg_temp |
|-----|------|----------|
| 09  | 12   | 27.4     |
| 09  | 13   | 28.1     |

## Repository Structure

IOT-SENSOR/
├── etl_job_1_clean_and_transform.py # Glue script for cleaning raw data
├── etl_job_2_aggregate_hourly_avg.py # Glue script for aggregating data
└── README.md

nginx
Copy
Edit



SATYAM SINGH RAJPUT 
Bachelor of Computer Applications (BCA), Sri Balaji University, Pune  
Specialization: Cloud & Cybersecurity  
GitHub: [@Satyam25613](https://github.com/Satyam25613)
