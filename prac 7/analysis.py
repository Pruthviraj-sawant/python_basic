import pandas as pd

# Create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 27, 22],
    'City': ['New York', 'San Francisco', 'Los Angeles']
}

df = pd.DataFrame(data)

# Display the DataFrame
print("Original DataFrame:")
print(df)

# Accessing specific columns
print("\nNames:")
print(df['Name'])

# Adding a new column
df['Salary'] = [50000, 60000, 45000]
print("\nDataFrame after adding Salary column:")
print(df)

# Filtering rows based on a condition
filtered_df = df[df['Age'] > 23]
print("\nFiltered DataFrame (Age > 23):")
print(filtered_df)

# Getting basic statistics
print("\nBasic statistics:")
print(df.describe())


