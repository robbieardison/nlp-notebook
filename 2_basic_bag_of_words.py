# NLP: Bag of Words and TF-IDF Vectorization

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

# Sample text data
texts = [
    "I hate natural language processing",
    "Natural language processing hates me",
    "I love spam emails"
]

print("Original Texts:")
for i, t in enumerate(texts):
    print(f"Text {i+1}: {t}")

# -------------------------------
# BAG OF WORDS
# -------------------------------
print("\n=== Bag of Words ===")
bow_vectorizer = CountVectorizer()
X_bow = bow_vectorizer.fit_transform(texts)

# Show the vocabulary
print("Vocabulary:", bow_vectorizer.get_feature_names_out())

# Show the word count vectors
print("BoW Vectors:")
print(X_bow.toarray())

# -------------------------------
# TF-IDF
# -------------------------------
print("\n=== TF-IDF ===")
tfidf_vectorizer = TfidfVectorizer()
X_tfidf = tfidf_vectorizer.fit_transform(texts)

# Show the vocabulary
print("Vocabulary:", tfidf_vectorizer.get_feature_names_out())

# Show the TF-IDF score vectors
print("TF-IDF Vectors:")
print(X_tfidf.toarray())
