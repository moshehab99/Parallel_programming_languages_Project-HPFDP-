# High-Performance Financial Data Processor (HPFDP)

## Project Overview
High-Performance Financial Data Processor (HPFDP) is a Python-based system designed to process large financial datasets efficiently using both **Parallel Processing** and **Sequential Processing** techniques.

The project allows users to compare traditional sequential execution with modern parallel execution to measure performance improvements when handling large-scale financial data.

The system uses:
- Parallel Processing
- Sequential Processing
- Batch Processing (Chunk-Based Reading)
- ETL Pipeline (Extract, Transform, Load)
- Graphical User Interface (GUI)

---

## Problem Statement
Processing large financial datasets sequentially can be slow and inefficient, especially with millions of records.

This project solves the problem by implementing:
- **Sequential Processing** for baseline comparison
- **Parallel Processing** for faster execution
- **Performance Comparison** between both approaches

---

## Project Objectives
- Process large financial datasets efficiently
- Compare Sequential vs Parallel execution
- Apply multiprocessing for high-speed processing
- Implement chunk-based batch processing
- Build ETL pipeline
- Store processed data into MySQL
- Provide user-friendly GUI interface

---

## Technologies Used
- Python
- Pandas
- SQLAlchemy
- MySQL
- PyMySQL
- CustomTkinter
- concurrent.futures (ProcessPoolExecutor)
- Threading

---

# System Workflow

## 1. Extract
Read large CSV file in chunks using:

```python
pd.read_csv(file_path, chunksize=5000)
```

This reduces memory usage and improves efficiency.

---

## 2. Transform
For each transaction:

- Calculate Tax (14%)
- Calculate Final Total Amount

```python
chunk['tax'] = chunk['amount'] * 0.14
chunk['total'] = chunk['amount'] + chunk['tax']
```

---

## 3. Load
Save processed data into MySQL database:

```python
to_sql()
```

---

# Processing Modes

## Sequential Processing (Standard Mode)
Data chunks are processed one by one in order.

### Advantages:
- Simple implementation
- Easy debugging
- Suitable for small datasets

### Disadvantages:
- Slower for huge datasets
- Does not utilize CPU cores efficiently

---

## Parallel Processing (Fast Mode)
Multiple chunks are processed simultaneously using multiple CPU cores.

Implemented using:

```python
from concurrent.futures import ProcessPoolExecutor
```

### Advantages:
- Faster execution
- Better CPU utilization
- Scalable for big data

### Disadvantages:
- More complex implementation
- Higher resource consumption

---

# Performance Comparison

The application allows direct comparison between both modes.

### Example Result:

- Sequential Processing: **89.91 seconds**
- Parallel Processing: **42.31 seconds**
- Performance Gain: **52.94% Faster**

Formula used:

```python
((Sequential Time - Parallel Time) / Sequential Time) * 100
```

---

# Batch Processing

Batch processing is implemented using:

```python
chunksize = 5000
```

### Benefits:
- Lower memory consumption
- Faster file reading
- Better scalability

---

# GUI Features

The system includes a modern graphical interface where users can:

- Select CSV file
- Run Parallel Processing
- Run Sequential Processing
- View processing status
- See execution time
- Compare performance gain

---

# Application Interface

![GUI Screenshot](images/gui.png)

---

# Example Console Output

```text
--- Starting Sequential Processing ---
Sequential Total: 1000000 rows in 89.91 seconds

--- Starting Parallel Processing ---
Parallel Total: 1000000 rows in 42.31 seconds

FINAL COMPARISON:
Sequential Mode: 89.91s
Parallel Mode:   42.31s
Performance Gain: 52.94% Faster!
```

---

# Project Structure

```text
HPFDP
│
├── processor.py
├── main_gui.py
├── data_generator.py
├── financial_data.csv
├── images
│   └── gui.png
└── README.md
```

---

# Key Concepts Demonstrated

- Multiprocessing
- Sequential Computing
- Parallel Computing
- ETL Pipeline
- Batch Processing
- GUI Development
- Database Integration
- Performance Optimization

---

# Future Improvements

- Add Real-Time Streaming using Kafka
- Distributed Processing with Spark
- Cloud Deployment
- Dashboard Analytics
- Export Reports
- Auto Benchmark Charts

---

# Team Members

- Mohamed Shehab Eldeen Khalil
- Mahmoud Mostafa Mohamed
- Mohamed Shady Aish
- Mostafa Ezzat Abd El-Naeem
- Saleh Saber Ebrahim

---

# Supervisor

Eng. El-Zahraa Eslam
