import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv(r"C:\Users\ME\OneDrive\Desktop\SuprMntr Internship Assignments\Mar9th\House_Price.csv")

print("----- DATASET -----\n")
print(df)

X = df[["Area", "Bedrooms"]]
y = df["Price"]

model = LinearRegression()
model.fit(X, y)

print("\nModel trained successfully!")

area = int(input("Enter area: "))
bedrooms = int(input("Enter bedrooms: "))

pred = model.predict([[area, bedrooms]])

print(f"\nPredicted price for house with {area} sqft and {bedrooms} bedrooms:")
print(pred[0])