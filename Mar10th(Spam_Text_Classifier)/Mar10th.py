import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load dataset
data = pd.read_csv("C:/Users/ME/OneDrive/Desktop/SuprMntr Internship Assignments/Mar10th(Spam_Text_Classifier)/Spam_Data.csv")

# Features and labels
X = data["Message"]
y = data["Label"]

# Convert text to numbers
vectorizer = CountVectorizer()
X_vector = vectorizer.fit_transform(X)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X_vector, y, test_size=0.2)

# Train model
model = MultinomialNB()
model.fit(X_train, y_train)

# Test with new message
msg = ["You won a free ticket"]
msg_vector = vectorizer.transform(msg)

prediction = model.predict(msg_vector)

print("Message:", msg[0])
print("Prediction:", prediction[0])