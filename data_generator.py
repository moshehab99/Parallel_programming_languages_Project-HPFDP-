import pandas as pd
import random

def generate_data(filename='financial_data.csv', rows=100000):
    print(f"Creating {rows} records...")
    data = {
        'transaction_id': range(1, rows + 1),
        'customer_name': [f'User_{i}' for i in range(1, rows + 1)],
        'amount': [round(random.uniform(100, 10000), 2) for _ in range(rows)],
        'type': [random.choice(['TRANSFER', 'PAYMENT', 'CASH_OUT']) for _ in range(rows)]
    }
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Done! File '{filename}' is ready.")

if __name__ == "__main__":
    generate_data()