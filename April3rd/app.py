import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer

st.title("NLP Keyword Extractor")

text = st.text_area("Enter your text:")

if st.button("Extract Keywords"):
    if text.strip() == "":
        st.write("Please enter text")
    else:
        vectorizer = TfidfVectorizer(stop_words='english')
        X = vectorizer.fit_transform([text])

        keywords = vectorizer.get_feature_names_out()

        st.write("Keywords:", keywords)