import pandas as pd

data = pd.read_csv("C:/Users/ME/OneDrive/Desktop/SuprMntr Internship Assignments/Feb26th/Employee_Dataset.csv")

print("----- ORIGINAL DATASET -----\n")
print(data)

print("\nMissing Values Before Cleaning:\n")
print(data.isnull().sum())

print("\nDuplicate Rows Before Cleaning:", data.duplicated().sum())

cleaned_data = data.copy()

cleaned_data = cleaned_data.fillna(method='ffill')

cleaned_data = cleaned_data.drop_duplicates()

for col in cleaned_data.select_dtypes(include='object').columns:
    cleaned_data[col] = cleaned_data[col].str.lower().str.strip()

print("\n----- CLEANED DATASET -----\n")
print(cleaned_data)

print("\nMissing Values After Cleaning:\n")
print(cleaned_data.isnull().sum())

print("\nDuplicate Rows After Cleaning:", cleaned_data.duplicated().sum())