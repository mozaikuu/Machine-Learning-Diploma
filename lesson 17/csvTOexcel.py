import pandas as pd

# Read the CSV file
df = pd.read_csv('Dataset.csv')

# Convert the CSV data to an Excel file
df.to_excel('output.xlsx', index=False)