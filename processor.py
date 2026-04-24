import pandas as pd
from sqlalchemy import create_engine
from concurrent.futures import ProcessPoolExecutor
import time


DB_URL = "mysql+pymysql://root:12345678@localhost/hpfdp_db"
engine = create_engine(DB_URL)

def process_chunk(chunk_data):
    chunk, chunk_id = chunk_data
    chunk['tax'] = chunk['amount'] * 0.14
    chunk['total'] = chunk['amount'] + chunk['tax']
    
    chunk.to_sql('transactions', con=engine, if_exists='append', index=False)
    return len(chunk)

def start_sequential_processing(file_path):
    print("\n--- Starting Sequential Processing (Standard Way) ---")
    start_time = time.time()
    
    reader = pd.read_csv(file_path, chunksize=5000)
    total_rows = 0
    
    for i, chunk in enumerate(reader):
        print(f"Processing Chunk #{i} sequentially...")
        total_rows += process_chunk((chunk, i)) 
        
    end_time = time.time()
    duration = round(end_time - start_time, 2)
    print(f"Sequential Total: {total_rows} rows in {duration} seconds.")
    return total_rows, duration

def start_parallel_processing(file_path):
    print("\n--- Starting Parallel Processing (High Performance) ---")
    start_time = time.time()
    
    reader = pd.read_csv(file_path, chunksize=5000)
    chunks_with_ids = [(chunk, i) for i, chunk in enumerate(reader)]
    
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(process_chunk, chunks_with_ids))
    
    end_time = time.time()
    duration = round(end_time - start_time, 2)
    print(f"Parallel Total: {sum(results)} rows in {duration} seconds.")
    return sum(results), duration

if __name__ == "__main__":
    file_name = 'financial_data.csv'
    
    seq_rows, seq_time = start_sequential_processing(file_name)
    
    par_rows, par_time = start_parallel_processing(file_name)
    
    print("\n" + "="*40)
    print(f"FINAL COMPARISON:")
    print(f"Sequential Mode: {seq_time}s ({seq_rows} rows)")
    print(f"Parallel Mode:   {par_time}s ({par_rows} rows)")
    if seq_time > 0:
        improvement = round(((seq_time - par_time) / seq_time) * 100, 2)
        print(f"Performance Gain: {improvement}% Faster!")
    else:
        print("Sequential time too low for meaningful gain comparison.")
    print("="*40)