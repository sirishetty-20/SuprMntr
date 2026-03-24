import pandas as pd
from sklearn.cluster import KMeans

# Load dataset (FIXED PATH)
data = pd.read_csv("C:/Users/ME/OneDrive/Desktop/SuprMntr Internship Assignments/Mar11th/mall_data.csv")

print("Dataset:\n")
print(data)

# Select features
X = data[["Annual Income", "Spending Score"]]

# Apply K-Means
kmeans = KMeans(n_clusters=3, random_state=0)
data["Cluster"] = kmeans.fit_predict(X)

print("\nClustered Data:\n")
print(data)

print("\nCluster Centers:\n", kmeans.cluster_centers_)