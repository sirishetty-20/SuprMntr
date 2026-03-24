import pandas as pd
from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv(r"C:\Users\ME\OneDrive\Desktop\SuprMntr Internship Assignments\Mar3rd\Student_data.csv")

# Features (Input) and Labels (Output)
X = df[["StudyHours"]]   # Feature
y = df["Marks"]          # Label

# Train model
model = LinearRegression()
model.fit(X, y)

# Prediction
predicted = model.predict([[6]])
print("Predicted marks for 6 study hours:", predicted[0])