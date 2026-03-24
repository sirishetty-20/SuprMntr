import string

# Sample stopwords list
stopwords = {
    'i','am','is','are','the','a','an','and','or','in','on','at','to','for',
    'of','with','this','that','it','be','as','was','were'
}

# Function to clean text
def clean_text(text):
    # Convert to lowercase
    text = text.lower()
    
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Tokenization (split into words)
    words = text.split()
    
    # Remove stopwords
    cleaned_words = [word for word in words if word not in stopwords]
    
    # Join words back
    cleaned_text = " ".join(cleaned_words)
    
    return cleaned_text

# Test the function
sample_text = "Hello!!! I am learning Python, and it is very interesting."

cleaned_output = clean_text(sample_text)

print("Original Text:")
print(sample_text)

print("\nCleaned Text:")
print(cleaned_output)