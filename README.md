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
- Architecture Patterns
- Design Patterns

---

## Problem Statement

Processing large financial datasets sequentially can be slow and inefficient, especially with millions of records.

This project solves the problem by implementing:

- **Sequential Processing** for baseline comparison
- **Parallel Processing** for faster execution
- **Performance Comparison** between both approaches
- **Architecture & Design Patterns** for better scalability and maintainability

---

## Project Objectives

- Process large financial datasets efficiently
- Compare Sequential vs Parallel execution
- Apply multiprocessing for high-speed processing
- Implement chunk-based batch processing
- Build ETL pipeline
- Store processed data into MySQL
- Provide user-friendly GUI interface
- Apply Software Engineering Principles
- Implement Architecture & Design Patterns

---

# Applied Architecture Pattern

## Layered Architecture

The project follows the **Layered Architecture Pattern** by separating the system into independent layers.

### Layers Used

### 1. Presentation Layer
Responsible for GUI interaction.

File:
```python
main_gui.py
```

### Responsibilities
- File selection
- Running processes
- Displaying status
- Showing performance comparison

---

### 2. Business Logic Layer
Responsible for processing logic.

Files:
```python
processor.py
strategies.py
```

### Responsibilities
- Sequential Processing
- Parallel Processing
- ETL Operations
- Strategy Management

---

### 3. Data Access Layer
Responsible for database communication.

File:
```python
database.py
```

### Responsibilities
- Database connection management
- MySQL interaction

---

## Benefits of Layered Architecture

- Better Maintainability
- Easier Debugging
- Clean Separation of Concerns
- Better Scalability
- Easier Future Enhancements

---

# Applied Design Patterns

## 1. Singleton Pattern

### Purpose
Ensure that only one database connection instance exists during runtime.

Implemented in:

```python
database.py
```

### Example

```python
class DatabaseConnection:
    _instance = None

    @staticmethod
    def get_instance():
        if DatabaseConnection._instance is None:
            DatabaseConnection._instance = create_engine(DB_URL)

        return DatabaseConnection._instance
```

### Benefits

- Reduces memory usage
- Prevents multiple DB connections
- Better resource management

---

## 2. Strategy Pattern

### Purpose
Allow switching dynamically between different processing algorithms.

Implemented in:

```python
strategies.py
```

### Strategies Used

- SequentialProcessingStrategy
- ParallelProcessingStrategy

### Example

```python
class ProcessingStrategy(ABC):

    @abstractmethod
    def process(self, file_path):
        pass
```

### Benefits

- Flexible architecture
- Easy to add new processing modes
- Cleaner code organization
- Follows Open/Closed Principle

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
- OOP
- Design Patterns

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

### Advantages

- Simple implementation
- Easy debugging
- Suitable for small datasets

### Disadvantages

- Slower for huge datasets
- Does not utilize CPU cores efficiently

---

## Parallel Processing (Fast Mode)

Multiple chunks are processed simultaneously using multiple CPU cores.

Implemented using:

```python
from concurrent.futures import ProcessPoolExecutor
```

### Advantages

- Faster execution
- Better CPU utilization
- Scalable for big data

### Disadvantages

- More complex implementation
- Higher resource consumption

---

# Performance Comparison

The application allows direct comparison between both modes.

### Example Result

| Mode | Time |
|------|------|
| Sequential Processing | 118.93 seconds |
| Parallel Processing | 25.68 seconds |

### Performance Gain Formula

```python
((Sequential Time - Parallel Time) / Sequential Time) * 100
```

---

# Batch Processing

Batch processing is implemented using:

```python
chunksize = 5000
```

### Benefits

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
- Demonstrate Design Patterns visually

---

# Application Interface

## Sequential Processing

<img width="1365" height="768" alt="Sequential Processing" src="./seq.png" />

---

## Parallel Processing

<img width="1365" height="768" alt="Parallel Processing" src="./parallel.png" />

---

# Example Console Output

```text
--- Starting Sequential Processing ---
Sequential Total: 1000000 rows in 118.93 seconds

--- Starting Parallel Processing ---
Parallel Total: 1000000 rows in 25.68 seconds

FINAL COMPARISON:
Sequential Mode: 118.93s
Parallel Mode:   25.68s
Performance Gain: 78.41% Faster!
```

---

# Project Structure

```text
HPFDP
│
├── main_gui.py
├── processor.py
├── strategies.py
├── database.py
├── data_generator.py
├── financial_data.csv
├── seq.png
├── parallel.png
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
- Layered Architecture
- Singleton Pattern
- Strategy Pattern
- OOP Principles

---

# Future Improvements

- Add Real-Time Streaming using Kafka
- Distributed Processing with Spark
- Cloud Deployment
- Dashboard Analytics
- Export Reports
- Auto Benchmark Charts
- Add Machine Learning Features
- Real-Time Monitoring System

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
