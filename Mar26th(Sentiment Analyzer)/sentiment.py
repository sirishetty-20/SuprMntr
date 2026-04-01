from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Step 1: Training Data (VERY IMPORTANT)
reviews = [
    "This movie is amazing and fantastic",
    "I loved the film, it was great",
    "What a wonderful experience",
    "I hate this movie, it was terrible",
    "Worst film ever",
    "Very boring and bad movie"
]

# Labels: 1 = Positive, 0 = Negative
labels = [1, 1, 1, 0, 0, 0]

# Step 2: Convert text into numbers
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(reviews)

# Step 3: Train model
model = MultinomialNB()
model.fit(X, labels)

# Step 4: Test on new reviews (your 5 reviews)
test_reviews = [
    "The movie was fantastic and I loved it",
    "It was a boring film",
    "Amazing story and great acting",
    "Worst movie I have seen",
    "It was okay but not great"
]

X_test = vectorizer.transform(test_reviews)

# Step 5: Predict
predictions = model.predict(X_test)

# Step 6: Output
for review, pred in zip(test_reviews, predictions):
    if pred == 1:
        print(review, "→ Positive 😊")
    else:
        print(review, "→ Negative 😞")