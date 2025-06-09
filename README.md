# IoT Sensor Data Processor

This project demonstrates an end-to-end ETL pipeline using AWS Glue and Amazon S3 to process IoT sensor data. It ingests raw sensor logs, performs data cleaning and transformation, calculates hourly temperature averages, and stores the results in an optimized format for analysis.

---

##  S3 Bucket Structure

s3://iot-sensor-data-satyam/

├── raw/ # Raw CSV or JSON sensor data

├── processed/ # Cleaned and transformed data in Parquet format

└── aggregated/ # Hourly average temperature data in Parquet format



---

##  Workflow Overview

### 1. Raw Data Ingestion
- Sensor logs (e.g., temperature, humidity) are uploaded to the `raw/` folder in CSV format.

### 2. ETL Job 1: Cleaning & Transformation
- Converts timestamps to standard format.
- Filters out faulty readings (temperature < -50°C or > 150°C).
- Writes cleaned data to `processed/` in Parquet format.

### 3. ETL Job 2: Aggregation
- Reads data from `processed/`.
- Extracts `hour` and `day` from timestamps.
- Calculates average temperature per hour.
- Writes aggregated output to `aggregated/`.

---

##  Technologies Used

- **AWS Glue** – Serverless ETL engine using PySpark
- **Amazon S3** – Cloud object storage
- **Apache Parquet** – Columnar format for efficient querying
- **PySpark** – Distributed data processing
- **GitHub** – Source control and collaboration

---

##  How to Use

1. **Upload Raw Data**
   - Place your sensor CSV files in: `s3://iot-sensor-data-satyam/raw/`

2. **Run ETL Jobs**
   - Run `iot_sensor_etl_job.py` via AWS Glue to create the cleaned dataset in `processed/`.
   - Run `iot_sensor_aggregate_job.py` to compute hourly average temperatures into `aggregated/`.

3. **Analyze the Data**
   - Use AWS Athena, QuickSight, or download the Parquet files to perform analytics.

---

##  Repository Structure

IOT-SENSOR/

├── iot_sensor_etl_job.py # Glue script for cleaning and transforming raw data

├── iot_sensor_aggregate_job.py # Glue script for hourly temperature aggregation

├── read_parquet.py # Python script to read Parquet output locally

└── README.md



---



**SATYAM SINGH RAJPUT**  
Bachelor of Computer Applications (BCA), Sri Balaji University, Pune  
Specialization: Cloud & Cybersecurity  
GitHub: [@Satyam25613](https://github.com/Satyam25613)
