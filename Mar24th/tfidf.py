from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

# Documents
docs = [
    "Machine learning is used for data analysis and prediction",
    "Deep learning improves machine learning models",
    "Data science uses machine learning and statistics",
    "Artificial intelligence includes machine learning and deep learning",
    "Statistics and data analysis are important in data science"
]

# TF-IDF (no stopword removal as you asked)
vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(docs)

df = pd.DataFrame(tfidf_matrix.toarray(), columns=vectorizer.get_feature_names_out())

print("TF-IDF Table:\n")
print(df)

# 🔥 Classification logic
print("\nWord Importance Classification:")

for i, doc in enumerate(df.values):
    print(f"\nDocument {i+1}:")
    
    for word, score in zip(df.columns, doc):
        if score > 0.4:
            level = "High Importance"
        elif score > 0.2:
            level = "Moderate Importance"
        elif score > 0:
            level = "Low Importance"
        else:
            continue
        
        print(f"{word} : {round(score,3)} → {level}")