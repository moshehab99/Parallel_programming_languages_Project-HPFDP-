from abc import ABC, abstractmethod
from concurrent.futures import ProcessPoolExecutor
import pandas as pd
import time

from database import DatabaseConnection

engine = DatabaseConnection.get_instance()


class ProcessingStrategy(ABC):

    @abstractmethod
    def process(self, file_path):
        pass



def process_chunk(chunk_data):
    chunk, chunk_id = chunk_data

    chunk['tax'] = chunk['amount'] * 0.14
    chunk['total'] = chunk['amount'] + chunk['tax']

    chunk.to_sql(
        'transactions',
        con=engine,
        if_exists='append',
        index=False
    )

    return len(chunk)


class SequentialProcessingStrategy(ProcessingStrategy):

    def process(self, file_path):
        print("\n--- Starting Sequential Processing ---")

        start_time = time.time()

        reader = pd.read_csv(file_path, chunksize=5000)

        total_rows = 0

        for i, chunk in enumerate(reader):
            print(f"Processing Chunk #{i} sequentially...")
            total_rows += process_chunk((chunk, i))

        duration = round(time.time() - start_time, 2)

        print(f"Sequential Total: {total_rows} rows in {duration} seconds.")

        return total_rows, duration


class ParallelProcessingStrategy(ProcessingStrategy):

    def process(self, file_path):
        print("\n--- Starting Parallel Processing ---")

        start_time = time.time()

        reader = pd.read_csv(file_path, chunksize=5000)

        chunks_with_ids = [
            (chunk, i)
            for i, chunk in enumerate(reader)
        ]

        with ProcessPoolExecutor() as executor:
            results = list(
                executor.map(process_chunk, chunks_with_ids)
            )

        duration = round(time.time() - start_time, 2)

        print(f"Parallel Total: {sum(results)} rows in {duration} seconds.")

        return sum(results), duration