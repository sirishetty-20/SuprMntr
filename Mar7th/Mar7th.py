from sklearn.neighbors import NearestNeighbors
import numpy as np

# Movie features: [Action, Romance]
data = np.array([
    [5, 1],  # Movie1
    [4, 1],  # Movie2
    [1, 5],  # Movie3
    [1, 4]   # Movie4
])

model = NearestNeighbors(n_neighbors=2)
model.fit(data)

# Find similar movies to Movie1
distance, index = model.kneighbors([[5, 1]])

print("Nearest Movies Index:", index)
print("Distances:", distance)