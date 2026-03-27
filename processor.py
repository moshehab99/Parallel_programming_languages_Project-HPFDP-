import pandas as pd
from sqlalchemy import create_engine
from concurrent.futures import ProcessPoolExecutor
import time

# 1. الربط بقاعدة البيانات (غير الباسورد لبسوردك الحقيقي)
DB_URL = "mysql+pymysql://root:12345678@localhost/hpfdp_db"
engine = create_engine(DB_URL)

def process_chunk(chunk_data):
    chunk, chunk_id = chunk_data
    print(f"Processing Chunk #{chunk_id}...")
    
    # الـ Transformation: حساب ضريبة 14%
    chunk['tax'] = chunk['amount'] * 0.14
    chunk['total'] = chunk['amount'] + chunk['tax']
    
    # الـ Load: حفظ في الداتابيز
    chunk.to_sql('transactions', con=engine, if_exists='append', index=False)
    return len(chunk)

def start_batch_processing(file_path):
    start_time = time.time()
    
    # الـ Batch Processing: تقسيم الملف لـ Chunks
    # الـ Parallelism: معالجة الـ Chunks بالتوازي
    reader = pd.read_csv(file_path, chunksize=5000)
    chunks_with_ids = [(chunk, i) for i, chunk in enumerate(reader)]
    
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(process_chunk, chunks_with_ids))
    
    end_time = time.time()
    print(f"Total processed: {sum(results)} rows in {round(end_time - start_time, 2)} seconds.")

if __name__ == "__main__":
    start_batch_processing('financial_data.csv')