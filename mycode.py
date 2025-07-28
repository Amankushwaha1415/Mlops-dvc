import os
import pandas as pd

# Step 1: Create 'data' folder if it doesn't exist
folder_name = 'data'
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Step 2: Create sample data using a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 22, 35, 28],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}
df = pd.DataFrame(data)

new_rows = [
    {'Name': 'Frank', 'Age': 26, 'City': 'Seattle'},
    {'Name': 'Grace', 'Age': 31, 'City': 'Boston'}
]

for row in new_rows:
    df.loc[len(df)] = row

# Step 3: Save the DataFrame as a CSV file in the 'data' folder
csv_path = os.path.join(folder_name, 'people.csv')
df.to_csv(csv_path, index=False)

print(f"CSV file created at: {csv_path}")
