# High-Performance Financial Data Processor (HPFDP)

## Project Overview
High-Performance Financial Data Processor (HPFDP) is a Python-based system designed to process large financial datasets efficiently using **parallel processing techniques**.

The system uses:
- Multiprocessing (parallel execution)
- Batch processing (chunk-based reading)
- ETL pipeline (Extract, Transform, Load)

---

## Problem Statement
Processing large financial datasets sequentially is slow and inefficient.  
This project solves this problem by applying parallel and batch processing to improve performance and scalability.

---

## Project Objectives
- Handle large financial datasets efficiently
- Apply multiprocessing for parallel execution
- Implement batch processing using chunking
- Build an ETL pipeline
- Store processed data in MySQL

---

## Technologies Used
- Python
- Pandas
- SQLAlchemy
- MySQL
- CustomTkinter (GUI)
- concurrent.futures (ProcessPoolExecutor)

---

## System Workflow

### 1. Extract
Read large CSV file using:
```python
pd.read_csv(file_path, chunksize=5000)
```

### 2. Transform
- Calculate Tax (14%)
- Calculate Total Amount

### 3. Load
Store processed data into MySQL database using:
```python
to_sql()
```

---

## Parallel Processing

- The dataset is divided into chunks
- Each chunk is processed in a separate process
- Processes run concurrently using:

```python
from concurrent.futures import ProcessPoolExecutor
```

---

## Batch Processing

Batch processing is implemented using:

```python
chunksize=5000
```

This allows efficient memory usage and faster processing.

---

## Application Interface

Below is a screenshot of the application GUI:

<img width="1206" height="907" alt="gui" src="https://github.com/user-attachments/assets/41de154a-c3eb-48f8-a2a5-b0dc62d27f88" />


---

## Example Output

- Processing chunks in parallel
- Saving results to MySQL
- Total processed rows displayed

---

## Project Structure

```
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

## Performance Advantage

Instead of processing data sequentially, the system processes chunks in parallel, significantly reducing execution time.

---

## Future Improvements
- Add real-time processing (Kafka)
- Distributed processing
- Analytics dashboard

---

## Team Members
- Mohamed Shehab Eldeen Khalil
- Mahmoud Mostafa Mohamed
- Mohamed Shady Aish
- Mostafa Ezzat Abd El-Naeem
- Saleh Saber Ebrahim
---

## Supervisor
Eng. El-Zahraa Eslam
