import pandas as pd

try:
    data = pd.read_csv("student-mat.csv")

    print("Top 5 Rows:\n")
    print(data.head())

    print("\nHighest Values in Each Column:\n")
    print(data.select_dtypes(include='number').max())

    print("\nMissing Values:\n")
    print(data.isnull().sum())

except FileNotFoundError:
    print("Error: CSV file not found. Check file name or path.")