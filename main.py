import pandas as pd
import os

data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35], 'City': ['New York', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)

## adding new row to df for v2
new_row = {'Name': 'David', 'Age': 40, 'City': 'San Francisco'}
df.loc[len(df)] = new_row

## adding new row to df for v3
new_row2 = {'Name': 'Eve', 'Age': 45, 'City': 'Seattle'}
df.loc[len(df)] = new_row2

data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

# Define the file path
file_path = os.path.join(data_dir, 'data.csv')

# Save df to csv using the same file_path variable
df.to_csv(file_path, index=False)

print(f"Data saved to {file_path}")