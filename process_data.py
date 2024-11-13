import pandas as pd

# Read the CSV file without headers, and manually set a column name
df = pd.read_csv('data.csv', header=None, names=['Name'])

# Strip any extra spaces from the 'Name' column
df['Name'] = df['Name'].str.strip()

# Print a complete description, including non-numeric columns
print(df.describe(include='all'))

# Optional: Check for unique values and their counts
print("\nUnique values count:")
print(df['Name'].nunique())

