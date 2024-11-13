import pandas as pd
import numpy as np

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
    'Age': [24, 27, 22, 32, np.nan, 29, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago', 'New York', 'Chicago', 'Los Angeles'],
    'Salary': [50000, 60000, 45000, 80000, 70000, 52000, np.nan]
}

df = pd.DataFrame(data)

# 1. Basic DataFrame Operations
print("Original DataFrame:")
print(df)

# 2. Handling missing data (filling missing values)
print("\nFilling missing values:")
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)
print(df)

# 3. Descriptive statistics
print("\nBasic Statistics:")
print(df.describe())

# 4. Filtering data based on a condition (people older than 25)
print("\nPeople older than 25:")
older_than_25 = df[df['Age'] > 25]
print(older_than_25)

# 5. Grouping and aggregating data (grouping by City)
print("\nGrouping by City (mean Age and Salary):")
grouped_by_city = df.groupby('City').agg({'Age': 'mean', 'Salary': 'mean'})
print(grouped_by_city)

# 6. Sorting data by Salary
print("\nSorting by Salary:")
sorted_df = df.sort_values(by='Salary', ascending=False)
print(sorted_df)

# 7. Adding a new column (Tax - 10% of Salary)
print("\nAdding 'Tax' column (10% of Salary):")
df['Tax'] = df['Salary'] * 0.10
print(df)

# 8. Exporting Data to a CSV file
output_file = 'people_data.csv'
df.to_csv(output_file, index=False)
print(f"\nData saved to '{output_file}'.")

# 9. Reading from a CSV file (demonstrating input/output)
print("\nReading from the saved CSV file:")
df_from_csv = pd.read_csv(output_file)
print(df_from_csv)

# 10. Advanced: Using apply function for custom transformations
print("\nApplying custom function to create a 'Seniority' column:")
df['Seniority'] = df['Age'].apply(lambda x: 'Senior' if x >= 30 else 'Junior')
print(df)
