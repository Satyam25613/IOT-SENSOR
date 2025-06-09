# IoT Sensor Data Processor

This project is part of the BCA curriculum at Sri Balaji University, Pune.  
It uses AWS services to build an ETL pipeline that processes sensor data for real-time environmental monitoring.

## 🔧 Project Stack
- AWS S3 (storage)
- AWS Glue (ETL scripting)
- Python (PySpark)
- GitHub (version control & submission)

## 📂 S3 Bucket Structure
iot-sensor-data-satyam/
├── raw/
│ └── Incoming raw sensor logs (CSV or JSON)
├── processed/
│ └── Cleaned data in Parquet format
└── aggregated/
└── Hourly/Daily averaged data in ORC or Parquet

## 🧠 ETL Logic (in Glue)
- Convert timestamp formats
- Filter out faulty readings (e.g., temperature < -50 or > 150)
- Calculate hourly and daily averages
- Save cleaned and aggregated output back to S3

## 📌 Status
Project repository structure ready. Code will be uploaded soon.
