import pandas as pd
import matplotlib.pyplot as plt

# Sample dataset
data = {
    "Name": ["Asha", "Rahul", "Priya", "Kiran", "Sneha"],
    "Marks": [85, 92, 78, 88, 95],
    "Attendance": [90, 85, 88, 92, 95]
}

df = pd.DataFrame(data)

# -------- Bar Chart --------
plt.figure()
plt.bar(df["Name"], df["Marks"])
plt.title("Marks of Students")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# -------- Pie Chart --------
plt.figure()
plt.pie(df["Marks"], labels=df["Name"], autopct="%1.1f%%")
plt.title("Marks Distribution")
plt.show()

# -------- Histogram --------
plt.figure()
plt.hist(df["Marks"])
plt.title("Marks Distribution Histogram")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()